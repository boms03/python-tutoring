def findsmallest(num_list):
    smallest=1000000
    for n in num_list:
        if smallest>n:
            smallest=n
    return smallest
print(findsmallest([4,7,2,5,8,1]))


def findlargest(nums_list):
    largest=-1
    for n in nums_list:
        print(largest,n)
        if largest<n:
            largest=n
            print(largest)
    return largest
print(findlargest([5,2,1,8,4,3]))
