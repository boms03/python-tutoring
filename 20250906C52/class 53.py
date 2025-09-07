def BubbleSort(numbs):
    for i in range(0,len(numbs)):
        for j in range(0,len(numbs)-i-1):
            if numbs[j]>numbs[j+1]:
                numbs[j],numbs[j+1]=numbs[j+1],numbs[j]
        print(numbs)
BubbleSort([6,3,4,1,2])

def InsertionSort(numbs):
    for i in range(1,len(numbs)):
        j=(i-1)
        number=numbs[i]
        while j>=0 and numbs[j]<number:
            numbs[j+1]=numbs[j]
            j=j-1
        numbs[j+1]=number
        print(numbs)
InsertionSort([1,8,5,7,6])

'''least to greatest'''
def SelectionSort(numbs):
    for i in range(0,len(numbs)):   
        minimum_index=i
        j=i+1
        while j<len(numbs):
            if numbs[j]>numbs[minimum_index]:
                minimum_index=j
            j=j+1
        numbs[i],numbs[minimum_index]=numbs[minimum_index],numbs[i]
        print(numbs)
SelectionSort([9,4,2,1,5,7])
        
           
        










'''
insertion sort

i - unsorted
for i in range(1, len(numbs)):

1 | 8  5  7  6
j   i 



j - sorted

comparing unsorted and sorted

i > j ---> swap

i < j ---> stay the same


for example:   1 | 8  5  7  6
                8 > 1

               1  8  | 5  7  6

ex:  1 | 8  5  7  6
    sorted | unsorted

    1. 1 < 8:

     1  8 | 5  7  6
    sorted | unsorted


    2. 5 < 8

    1  5  8  |  7   6 

        AND

       1 < 5:

     1  5  8  |  7   6


    3. 7 < 8

    1  5  7  8  |  6

       5 < 7

    1  5  7  8  |  6

       1  < 7

    1  5  7  8  |  6


    4. 6 < 8

    1  5  7  6  8

       6 < 7

    1  5  6  7  8

       5 < 6

    1  5  6  7  8



= 1 5 6 7 8

    
'''
