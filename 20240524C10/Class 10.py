fruitslist = ['apple', 'banana', 'grape', 'kiwi']

#problem1 print grape
for fruit in fruitslist:
    if fruit=='grape':
        print(fruit)
        
#problem2 count the number of loop
count=0
for fruit in fruitslist:
    count=count+1
print(count)

#problem3 count b, a, n
count=0
b=0
a=0
n=0
for fruit in fruitslist:
    count=count+1
    if count==2:
        for alphabet in fruit:
            if alphabet=='b':
                b=b+1
            elif alphabet=='a':
                a=a+1
            elif alphabet=='n':
                n=n+1
print(b)
print(a)
print(n)
