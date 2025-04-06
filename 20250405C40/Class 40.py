numberlist=list(map(int,input().split()))
for i in range(0,len(numberlist)):
    target=numberlist[i]
    j=i-1
    while j>=0 and numberlist[j]<target:
        numberlist[j+1]=numberlist[j]
        j=j-1
    numberlist[j+1]=target
    print(numberlist)


'Homework: Step By Step'

'Homework: think about what you can change in the selection sort so it descends'
