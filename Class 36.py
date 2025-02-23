#for all index i < j < z, find all triplets nums[i] > nums[j] > nums[z]

nums=[5,10, 2, 17, 1,20, 13, 3]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        for z in range(j+1,len(nums)):
            if nums[i]>nums[j]>nums[z]:
                print(nums[i],nums[j],nums[z])
        

               
