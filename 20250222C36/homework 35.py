i=int(input())
for star in range(1,i):
    print((' '*(i-star)),('*'*(star*2-1)))   
for star in range(i-2,0,-1):         
    print((' '*(i-star)),('*'*(star*2-1)))

'''9-7
7-2
9-6
6-2'''

    



'''i=int(input())
for star in range(i,0,-1):
    print('*'* star)'''
'''
i=int(input())
for star in range(1,i):
    print((' '*(i-star)),('*'*(star*2-1)),(' '*(i+star)),('*'*(star-2)))
    ----->failed '''









'''+2 each time
                  * --->1
                 *** --->3
   ***** --->5
  ******* --->7
********* --->9
              
               ******* --->7     1,7
                ***** --->5      2,5
                 *** --->3       3,3
                  * --->1        4,1
                  
                      '''

'''i=int(input())
for star in range(1,i):
    print((' ' *(i-1-star)),('*'*(star*2-1)))'''
