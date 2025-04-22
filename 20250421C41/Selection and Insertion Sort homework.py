Insertion Sort
- target        

numberlist=list(map(int,input().split()))
for i in range(0,len(numberlist)):
    target=numberlist[i]
    j=i-1
    while j>=0 and numberlist[j]<target:
        numberlist[j+1]=numberlist[j]
        j=j-1
        numberlist[j+1]=target        
    print(numberlist)


Step by Step with numbers 8 2 6 3 4:

1. 8  2  6  3  4
j  i

i = 0
j= -1

    target=numberlist[0]=8
    j=i-1
    while j>=0 -->NO and numberlist[j]<target --> No:

    print(numberlist)


2. 8  2  6  3  4
   j  i

i=1
j=0

    target=numberlist[1]=2
    j=i-1
    while 0>=0 --> YES and numberlist[8]<target --> NO:

    print(numberlist)
    

3. 8  2  6  3  4
      j  i
i=2
j=1

    target=numberlist[2]=6
    j=i-1
    while 1>=0 --> YES and numberlist[1]<6 --> YES:
        numberlist[1+1]=numberlist[1] --> 8  2  6  3  4 --> 8  2  2  3  4
                                                
        j=j-1 --> 8  2  2  3  4

    while 0>=0 --> YES and numberlist[0 =8]<6 --> NO:
                     
        numberlist[0+1]=target --> 8  2  2  3  4 --> 8  6  2  3  4


4. 8  6  2  3  4
         j  i

i = 3
j = 2

    target=numberlist[3]=3
    j=i-1
    while 2>=0 --> YES and numberlist[2]<3 --> YES:
        numberlist[2+1]=numberlist[2] --> 8  6  2  2  4
                                      
        j=j-1 --> 8  6  2  2  4
                     j

    while 1>=0 --> YES and numberlist[1]<3 --> NO:
        
        numberlist[j+1]=target --> 8  6  2  2  4 ---> 8  6  3  2  4

5. 8  6  3  2  4
            j  i

i= 4
j=3
    target=numberlist[4]
    j=i-1
    while 3>=0 --> YES and numberlist[3]<4 --> YES
        numberlist[3+1]=numberlist[3]--> 8  6  3  2  2
                                                    
        j=j-1 --> 8 6 3 2 2
                      j i

    while 2>=0 --> YES and numberlist[2]<4 --> YES
        numberlist[2+1]=numberlist[2] --> 8  6  3  3  2

        j = j-1 --> 8 6 3 3 2
                      j

    while 1>=0 --> YES and numberlist[1]<4 --> NO
    
        numberlist[j+1]=target --> 8  6  4  3  2 
                                      j  
                                     

    
Selection Sort
- minimum_index 

numberlist=list(map(int,input().split()))
for i in range(len(numberlist)):
    maximum_index=i
    for j in range(i+1,len(numberlist)):
        if numberlist[j]>numberlist[maximum_index]:
            maximum_index=j
    numberlist[maximum_index],numberlist[i]=numberlist[i],numberlist[maximum_index]
    print(numberlist)


Step by Step: 8 2 6 3 4


1. 8 | 2  6  3  4
   i   j

i = 0
j = 1
   maximum_index=0
       if numberlist[1]>numberlist[0] --> NO
       if numberlist[2]>numberlist[0] --> NO
       if numberlist[3]>numberlist[0] --> NO
       if numberlist[4]>numberlist[0] --> NO
    numberlist[maximum_index],numberlist[i]=numberlist[i],numberlist[maximum_index]
    print(numberlist) --> 8  2  6  3  4

2. 8  2 | 6  3  4
      i  j
   maximum_index=1
       if numberlist[2]>numberlist[1] --> YES
       maximum_index= 2
       if numberlist[3]>numberlist[2] --> NO
       if numberlist[4]>numberlist[2] --> NO

       numberlist[maximum_index],numberlist[i]=numberlist[i],numberlist[maximum_index]
       
       ---> 8  6  2  3  4
       print(numberlist) --> 8  6  2  3  4

3. 8  6  2 | 3  4
         i   j 
    maximum_index=2
        if numberlist[3]>numberlist[2] --> YES
        maximum_index=3
        if numberlist[4]>numberlist[3] --> YES
        maximum_index=4
        
    numberlist[maximum_index],numberlist[i]=numberlist[i],numberlist[maximum_index]
    ---> 8 6 4 3 2

8  6  4  3  2

        
         
         
    
    

        

   
    
