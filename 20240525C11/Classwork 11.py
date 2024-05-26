#problem1 print even numbers in between 1-21
n=0
while n<21:
    n=n+1
    if n%2==0:
        print(n)
#problem2 print odd numbers in between 1-21
n=0
while n<21:
    n=n+1
    if n%2==1:
        print(n)
#problem3 print odd numbers in between 1-21 using break
n=0
while True:
    if n>21:
        break
    n=n+1
    if n%2==1:
        print(n)
#problem4 print even numbers in between given inputs and using break
a=int(input())
b=int(input())
n=a
while True:
    if n>b:
        break
    if n%2==1:
        print(n)
    n=n+1
        
    
    
    
    
