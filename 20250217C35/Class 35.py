'''i=int(input())
for star in range(1,i):
    print('*'* star)'''

'''i=int(input())
for star in range(i,0,-1):
    print('*'* star)'''
    
'''i=int(input())
for star in range(1,i+1):
    print((' '*(i-star)),('*'* star))'''

i=int(input())
for star in range(1,i):
    print((' ' *(i-1-star)),('*'*(star*2-1)))


'''+2
     * 1
    *** 3
   ***** 5
  ******* 7
 ********* 9'''
