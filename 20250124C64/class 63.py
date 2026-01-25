fruitlist = ['apple', 'banana', 'strawberry', 'apple', 'apple']
def countFruit(fruitlist, val):
    for fruit in fruitlist:
        count=0
        if fruit==val:
            count=count+1
    return count
print(countFruit(fruitlist, 'banana'))




animalList= ['goat', 'sheep', 'sheep', 'goat', 'goat', 'goat', 'sheep']
print(animalList)
for i in range(0,len(animalList)): 
    if animalList[i]=='goat':
        animalList[i]='fox'

for i in range(0, len(animalList)):
    if animalList[i]=='sheep':
        animalList[i]='goat'

for i in range(0, len(animalList)):
    if animalList[i]=='fox':
        animalList[i]='sheep'
print(animalList)




numberList = [1, 3, 5, 7, 9]
i = numberList[2]
j = numberList[4]

'''swapping(i,j) swapping the two input, i and j

    ex. (0,3) in [0, 1, 3, 6, 9] --> [3, 1, 0, 6, 9]'''
for number in range(0, len(numberList)):
    if numberList[number]==i:
                    numberList[number]= j
for number in range(0, len(numberList)):
    if numberList[number]==j:
                    numberList[number]=i
print(numberList)

''' --> [1, 3, 5, 7, 9] to [1, 3, 5, 7, 5]'''


numberList = [1, 3, 5, 7, 9]
i = numberList[2] 
j = numberList[4]
for number in range(0, len(numberList)):
    if numberList[number]==i:
        numberList[number]= 'swap'
for number in range(0, len(numberList)):
    if numberList[number]==j:
        numberList[number]=i
for number in range(0, len(numberList)):
    if numberList[number]=='swap':
        numberList[number]=j 
print(numberList)



numberList = [1, 3, 5, 5, 9]
print(numberList)
def swap(i,j, numberList):
    temp= numberList[j]
    numberList[j]=numberList[i]
    numberList[i] = temp
swap(2,4, numberList)
print(numberList)
    

'''    
    temp = numberList[i]
    numberList[i] = numberList[j]
    numberList[j] = temp'''





numberList= [1,3,5,5,9]
def reverse(numberList):
    '''    1. 0, len(numberList)-1
    2. 0+1, len(numberList)-2
    3. 0+2, len(numberList)-3'''
    
    Left = 0
    Right = len(numberList)-1
    while Left<Right:
        temp=numberList[Right]
        numberList[Right]=numberList[Left]
        numberList[Left]=temp
        Left = Left+1
        Right = Right-1
print(numberList)
reverse(numberList)
print(numberList)
        
    
    
    











    

