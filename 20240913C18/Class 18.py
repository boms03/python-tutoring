fruitlist = ['strawberry', 'apple', 'kiwi', 'blueberry','rasberry']
'''for fruit in fruitlist:
    print(fruit)
index=0
while True:
    if index==len(fruitlist):
        break   
    print(fruitlist[index])
    index=index+1
    
index=0
while index<len(fruitlist):
    print(fruitlist[index])
    index=index+1'''
'''index=0
while index<len(fruitlist):
    if index%2==0:
       print(fruitlist[index])
    index=index+1
 
index=0
while index<len(fruitlist):
    if index%2 ==1:
        print(fruitlist[index])
    index=index+1


index=0
while True:
    if index==len(fruitlist):
        break
    if index%2==0:
        print(fruitlist[index])
    index=index+1

index=0
while True:
    if index==len(fruitlist):
        break
    if index%2==1:
        print(fruitlist[index])
    index=index+1'''
        
        
'''for index,fruit in enumerate(fruitlist):
    print(index, fruit)

index=0
while index<len(fruitlist):
    print(index,fruitlist[index])
    index=index+1'''
numberlist=[]
i = input().split()
print(i)
for y in i:
    numberlist.append(int(y))
print(numberlist)


a,b=map(int, input().split())
print(a,b)
