import { createServer } from "node:http";
import { scryptSync, randomBytes, timingSafeEqual } from "node:crypto";

// 메모리 저장소 (데모용 - 재시작하면 사라짐)
const users = new Map();    // username -> { salt, hash }
const sessions = new Map(); // sid -> username
const images = new Map();   // imageId -> { type, data(Buffer) }
const posts = [];           // { id, caption, imageId, author, createdAt }
let nextPostId = 1;

const MAX_IMAGE_BYTES = 5 * 1024 * 1024; // 5MB
const ALLOWED_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"];

// ---------- helpers ----------

// Safari 호환: SameSite=Lax (first-party 쿠키), HTTPS일 때만 Secure
// Partitioned / SameSite=None 제거 (Safari는 서드파티 쿠키를 차단함)
const isSecure = (req) =>
    req.headers["x-forwarded-proto"] === "https" || Boolean(req.socket.encrypted);

const cookieAttrs = (req) =>
    isSecure(req)
        ? "HttpOnly; Secure; SameSite=Lax; Path=/"
        : "HttpOnly; SameSite=Lax; Path=/";

const esc = (s) =>
    String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

const layout = (user, body) => `
  <div style="padding: 2px 20px; font-family: system-ui; max-width: 480px">
    <nav style="display: flex; gap: 12px; align-items: center; margin: 16px 0;">
      <a href="/" style="color: #5C6AC4;">Home</a>
      ${
    user
        ? `<span style="margin-left: auto;">${esc(user)}</span>
             <form method="POST" action="/logout" style="margin: 0;"><button>Logout</button></form>`
        : `<a href="/login" style="color: #5C6AC4;">Login</a>
             <a href="/signup" style="color: #5C6AC4;">Sign Up</a>`
}
    </nav>
    ${body}
  </div>
`;

const formStyle = "display: flex; flex-direction: column; gap: 12px;";
const inputStyle = "padding: 8px;";
const btnStyle = "padding: 8px; background: #5C6AC4; color: white; border: 0; cursor: pointer;";
const errorMsg = (m) => (m ? `<p style="color: crimson;">${esc(m)}</p>` : "");

const readBuffer = (req, limit) =>
    new Promise((resolve) => {
        const chunks = [];
        let size = 0;
        let tooLarge = false;
        req.on("data", (chunk) => {
            size += chunk.length;
            if (size > limit) tooLarge = true;
            else chunks.push(chunk);
        });
        req.on("end", () => resolve(tooLarge ? null : Buffer.concat(chunks)));
        req.on("error", () => resolve(null));
    });

const readForm = async (req) => new URLSearchParams((await readBuffer(req, 10_000))?.toString() ?? "");

const send = (res, status, type, body, headers = {}) => {
    res.writeHead(status, { "Content-Type": type, ...headers });
    res.end(body);
};
const html = (res, status, body) => send(res, status, "text/html; charset=utf-8", body);
const json = (res, status, obj) => send(res, status, "application/json", JSON.stringify(obj));
const redirect = (res, to, headers = {}) => {
    res.writeHead(303, { Location: to, ...headers });
    res.end();
};

const getSid = (req) => /(?:^|;\s*)sid=([^;]+)/.exec(req.headers.cookie ?? "")?.[1] ?? null;
const getUser = (req) => sessions.get(getSid(req)) ?? null;

const verifyPassword = (password, { salt, hash }) =>
    timingSafeEqual(scryptSync(password, salt, 64), Buffer.from(hash, "hex"));

// ---------- pages ----------
const homePage = (user) =>
    layout(
        user,
        `<div style="display: flex; align-items: center; justify-content: space-between;">
       <h1 style="color: #5C6AC4;">Posts</h1>
       ${
            user
                ? `<a href="/posts/new"
                style="padding: 8px 14px; background: #5C6AC4; color: white; text-decoration: none; border-radius: 4px;">
                + Create New Post
              </a>`
                : ""
        }
     </div>
     ${
            posts.length === 0
                ? "<p>아직 글이 없습니다.</p>"
                : [...posts]
                    .reverse()
                    .map(
                        (p) => `
         <article style="border-bottom: 1px solid #ddd; padding: 12px 0;">
           <img src="/images/${p.imageId}" alt="" style="width: 100%; border-radius: 6px;" />
           <p style="white-space: pre-wrap; margin: 8px 0 4px;">${esc(p.caption)}</p>
           <small>by ${esc(p.author)} · ${p.createdAt.toLocaleString()}</small>
         </article>`
                    )
                    .join("")
        }`
    );

const signupPage = (user, error) =>
    layout(
        user,
        `<h1 style="color: #5C6AC4;">Sign Up</h1>
     ${errorMsg(error)}
     <form method="POST" action="/signup" style="${formStyle}">
       <input name="username" placeholder="Username" required style="${inputStyle}" />
       <input name="password" type="password" placeholder="Password" required style="${inputStyle}" />
       <button style="${btnStyle}">Sign Up</button>
     </form>`
    );

const loginPage = (user, error) =>
    layout(
        user,
        `<h1 style="color: #5C6AC4;">Login</h1>
     ${errorMsg(error)}
     <form method="POST" action="/login" style="${formStyle}">
       <input name="username" placeholder="Username" required style="${inputStyle}" />
       <input name="password" type="password" placeholder="Password" required style="${inputStyle}" />
       <button style="${btnStyle}">Login</button>
     </form>`
    );

const newPostPage = (user) =>
    layout(
        user,
        `<h1 style="color: #5C6AC4;">New Post</h1>
     <p id="error" style="color: crimson;"></p>
     <form id="post-form" style="${formStyle}">
       <input id="photo" type="file" accept="image/jpeg,image/png,image/gif,image/webp" required />
       <img id="preview" alt="" style="display: none; width: 100%; border-radius: 6px;" />
       <textarea id="caption" placeholder="Caption" required rows="3" maxlength="500" style="${inputStyle}"></textarea>
       <button id="submit" style="${btnStyle}">Publish</button>
     </form>
     <script>
       const photo = document.getElementById("photo");
       const preview = document.getElementById("preview");
       const error = document.getElementById("error");

       photo.addEventListener("change", () => {
         const file = photo.files[0];
         if (!file) return;
         preview.src = URL.createObjectURL(file);
         preview.style.display = "block";
       });

       document.getElementById("post-form").addEventListener("submit", async (e) => {
         e.preventDefault();
         error.textContent = "";
         const file = photo.files[0];
         const caption = document.getElementById("caption").value.trim();
         if (!file || !caption) return;

         const submit = document.getElementById("submit");
         submit.disabled = true;
         try {
           const res = await fetch("/posts?caption=" + encodeURIComponent(caption), {
             method: "POST",
             headers: { "Content-Type": file.type },
             body: file,
             credentials: "same-origin",
           });
           if (res.ok) {
             location.href = "/";
             return;
           }
           error.textContent = (await res.json()).error ?? "업로드에 실패했습니다.";
         } catch {
           error.textContent = "네트워크 오류가 발생했습니다.";
         }
         submit.disabled = false;
       });
     </script>`
    );

// ---------- server ----------
const server = createServer(async (req, res) => {
    const url = new URL(req.url, "http://localhost");
    const { pathname } = url;
    const user = getUser(req);

    // 이미지 서빙: GET /images/:id
    if (req.method === "GET" && pathname.startsWith("/images/")) {
        const image = images.get(pathname.slice("/images/".length));
        if (!image) return html(res, 404, layout(user, "<h1>404 Not Found</h1>"));
        return send(res, 200, image.type, image.data, { "X-Content-Type-Options": "nosniff" });
    }

    switch (`${req.method} ${pathname}`) {
        case "GET /":
            return html(res, 200, homePage(user));

        // --- 회원가입 ---
        case "GET /signup":
            return html(res, 200, signupPage(user));

        case "POST /signup": {
            const params = await readForm(req);
            const username = params.get("username")?.trim();
            const password = params.get("password");

            if (!username || !password) return html(res, 400, signupPage(user, "username과 password를 입력해주세요."));
            if (users.has(username)) return html(res, 409, signupPage(user, "이미 존재하는 username입니다."));

            const salt = randomBytes(16).toString("hex");
            users.set(username, { salt, hash: scryptSync(password, salt, 64).toString("hex") });
            return redirect(res, "/login");
        }

        // --- 로그인 / 로그아웃 ---
        case "GET /login":
            return html(res, 200, loginPage(user));

        case "POST /login": {
            const params = await readForm(req);
            const username = params.get("username")?.trim();
            const record = users.get(username);

            if (!record || !verifyPassword(params.get("password") ?? "", record)) {
                return html(res, 401, loginPage(user, "username 또는 password가 올바르지 않습니다."));
            }

            const sid = randomBytes(24).toString("hex");
            sessions.set(sid, username);
            return redirect(res, "/", { "Set-Cookie": `sid=${sid}; ${cookieAttrs(req)}` });
        }

        case "POST /logout":
            sessions.delete(getSid(req));
            return redirect(res, "/", { "Set-Cookie": `sid=; Max-Age=0; ${cookieAttrs(req)}` });

        // --- 글쓰기 (사진 + caption) ---
        case "GET /posts/new":
            if (!user) return redirect(res, "/login");
            return html(res, 200, newPostPage(user));

        case "POST /posts": {
            if (!user) return json(res, 401, { error: "로그인이 필요합니다." });

            const type = (req.headers["content-type"] ?? "").split(";")[0].trim();
            const caption = url.searchParams.get("caption")?.trim();

            if (!ALLOWED_TYPES.includes(type)) return json(res, 415, { error: "jpg, png, gif, webp 이미지만 업로드할 수 있습니다." });
            if (!caption) return json(res, 400, { error: "caption을 입력해주세요." });
            if (caption.length > 500) return json(res, 400, { error: "caption은 500자 이하여야 합니다." });

            const data = await readBuffer(req, MAX_IMAGE_BYTES);
            if (!data) return json(res, 413, { error: "이미지는 5MB 이하여야 합니다." });
            if (data.length === 0) return json(res, 400, { error: "이미지가 비어 있습니다." });

            const imageId = randomBytes(12).toString("hex");
            images.set(imageId, { type, data });
            posts.push({ id: nextPostId++, caption, imageId, author: user, createdAt: new Date() });
            return json(res, 201, { ok: true });
        }

        // --- API ---
        case "GET /api/hello":
            return json(res, 200, { message: "Hello, World!" });

        default:
            return html(res, 404, layout(user, "<h1>404 Not Found</h1>"));
    }
});

server.listen(3000, "0.0.0.0", () => {
    console.log("Server listening on port 3000");
});