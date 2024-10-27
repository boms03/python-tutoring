list=list(map(int,input().split()))
print(list)
for idx,i in enumerate(list):
    if idx==0:
        continue
    print("parentNode is ",i)
    if idx*2>=len(list):
        print("no left child")
    else:
        print("leftchild is ", list[idx*2])
    if idx*2+1>=len(list):
        print("no right child")
    else:
        print("rightchild is ", list[idx*2+1])
    
    
    
    

