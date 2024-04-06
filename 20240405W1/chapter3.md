# Installing Python

1. go to https://www.python.org/


<p align=center>
    <img src="img.png" width="500">
</p>

2. Click Download - Windows


<p align=center>
    <img src="img_1.png" width="500">
</p>

3. Choose Python 3.11.9


4. After you download the Windows installer, double-click its icon, and then follow the instructions to install Python in the default location, as follows:
    1. Select Install for All Users, and then click Next.
    2. Leave the default directory unchanged, but note the name of the installation directory
    3. (probably C:\Python31 or C:\Python32)
    4. Click Next.
    5. Ignore the Customize Python section of the installation, and
       click Next.


5. At the end of this process, you should have a Python 3 entry in
   your Start menu

<p align=center>
    <img src="img_2.png" width="500">
</p>

# Shell vs Code editor

<p align=center>
    <img src="img_3.png" width="500">
</p>

- This is the Python shell
- The three greater-than signs (>>>) are called the prompt
- Runs the code **line by line**
- You cannot save the code

<p align=center>
    <img src="img_4.png" width="500">
</p>

<p align=center>
    <img src="img_5.png" width="500">
</p>

- This is the code editor
- Run **all** the codes
- You can save the code now!
- Ctrl+S to save
- F5 (fn + f5) to run to your code

# Strings

- A string is a collection of letters
- All the letters, numbers, and symbols could be a string.
- Use double or single quotations!

<p align=center>
    <img src="img_6.png" width="800">
</p>

<p align=center>
    <img src="img_7.png" width="800">
</p>

- to see what’s inside fred, we could enter print(fred)

<p align=center>
    <img src="img_8.png" width="800">
</p>

- You can also use single quotes to create a string

# Quiz 1

<p align=center>
    <img src="img_9.png" width="800">
</p>

Will this prompt work?

<details>
    <summary>Answer</summary>

No! it generates **SyntaxError**

<p align=center>
    <img src="img_16.png" width="800">
</p>

- Syntax means the arrangement and order of words in a sentence
- SyntaxError means that you did something in an order Python was not expecting
- In this case, Python did not find **a double quote** to close the string.

</details>


# Multiline String

- Use three single quotes (''')

<p align=center>
    <img src="img_10.png" width="800">
</p>

<p align=center>
    <img src="img_11.png" width="800">
</p>

# Quotations Inside Quotations

- You cannot **just** use quotations in quotations

<p align=center>
    <img src="img_12.png" width="800">
</p>

- How to **distinguish** the inside quotations?

# Challenge 1

First declare the **silly_string** above

Use **\** to distinguish the inside quotations

<details>
    <summary>Answer</summary>
    <p align=center>
        <img src="img_13.png" width="800">
    </p>
    
</details>


# Embedding Values in Strings

- replace **placeholder** %s with a variable

<p align=center>
    <img src="img_14.png" width="800">
</p>

# Quiz 2

<p align=center>
    <img src="img_15.png" width="800">
</p>

What is the output?

You can try in Python Shell

<details>
    <summary>Answer</summary>

    Knee: a device for finding furniture in the dark
    
    This is same as print('%s: a device for finding furniture in the dark’  % 'Knee’)
    
</details>


