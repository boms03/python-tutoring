B=list(map(int,input().split()))
for i in range(len(B)):
    minimum_index=i
    for j in range(i+1,len(B)):
        if B[j]<B[minimum_index]:
            minimum_index=j
    B[i],B[minimum_index]=B[minimum_index],B[i]
    print(B)
            
'''Homework:  
Write step by step for = 7 9 4 3 1'''


'''

B= the input list

for i in range(len(B)) --> i=0 to the length of the list
    the minimum_index is i
for j in range(i+1, len(B)) --> j= i+1 to the length of the list

    if B[i]is less than B[minimum_index(or smallest number):
        than the minimum_index  is j
    B[i], B[minimum_index]=B[minimum_index],B[i] --> SWAP

STEP BY STEP:

1.      7 | 9  4  3  1

    if B[7]< B[1]--> X

    == so the 7 and 1 SWAP places

2.      1  9 | 4  3  7

    if B[9]<B[4 is less than nine, but so is 3] --> X

    === so the 9 and the 3 AND 4 SWAP places

3.      1  3  4 | 9  7

    if B[9]<B[7] --> X

    === so the 9 and the 7 SWAP places
    
4.      1  3  4  7|  9

    if B[9]<B[9] --> wait they're equal

    == so the 9 stays in the same place

5.      1  3  4  7  9

ALL DONE! THEY ARE ALL SORTED
    

'''
