n=list(map(int,input().split()))
target=int(input())
n.sort()
l=0
r=len(n)-1
while l<r:
    if n[l]+n[r]<target:
        l=l+1
    elif n[l]+n[r]>target:
        r=r-1
    else:
        print(n[l],n[r])
        break


'''
n = input(input is a list)
(find two paris ex. 5 and 3) that = n

l= (zero)
r=len(list)-1




'''
