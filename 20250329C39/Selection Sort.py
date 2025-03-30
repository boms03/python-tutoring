B=list(map(int,input().split()))
for i in range(len(B)):
    minimum_index=i
    for j in range(i+1,len(B)):
        if B[j]<B[minimum_index]:
            minimum_index=j
    B[i],B[minimum_index]=B[minimum_index],B[i]
    print(B)
            
Homework:  
Write step by step for = 7 9 4 3 1
