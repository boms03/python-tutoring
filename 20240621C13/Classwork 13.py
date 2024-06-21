#for loop

foodList = ["pizza", "sushi", "pasta"]

# Problem1: for loop foodList and print each
for food in foodList:
    print(food)

# Problem2: for loop range from 3 to 30 by step 4
# range(a,b) -> from a to b-1
# range(a,b,c) -> from a to b-1 by step 2
for i in range(3,30,4):
    print(i)

# Problem3: for loop range from 0 to 30 and print even numbers only

for i in range(0,30):
    if (i%2==0):
        print(i)
