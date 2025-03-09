
'''this is an empty list where I will put the zeros in'''

'''this is the input of where I will input a string
of numbers to use the code for, but I put int() in the front
so that the number string can be numbers instead of a string.'''

number=list(map(int,input().split()))
newlist=[]
for i in range(0,len(number)):
    if len(newlist)==len(number):
        break
    if number[i]==0:
        newlist.append(number[i])
        newlist.append(number[i])
    else:
        newlist.append(number[i])
print(newlist)

