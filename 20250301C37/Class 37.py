answer=[]
temperatures=list(map(int,input().split()))
for i in range(0,len(temperatures)):
    foundAnswer=False
    for j in range(i+1,len(temperatures)):
        if temperatures[j]>temperatures[i]:
            answer.append(j-i)
            foundAnswer=True
            break
    if not foundAnswer:
        answer.append(0)
print(answer)
'''
1. split the strings
2. convert each string to int(map+int)
3. convert to list

Brute Force:
1. i = start from 0 to len of temperatures
2. j = start from the one after i(i+1) to len of temperatures
you have to start from i+1 because you are comparing every pair once to see the increase of temperature
3. you find the answer when the value of temperatures at index j is greater than the value of temperatures at index i
4. to the answer list, you are appending the difference of the index of the temperatures.

Flag:
*You need to use flag to track no growth in the temperatures

'''

