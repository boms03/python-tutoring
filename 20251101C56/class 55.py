'''
num_list = [1, 3, 5, 7, 9, 11, 13, 15]

def binarysearch(value):
    left = 0
    right= len(num_list)-1
    while left<=right:
        mid=(left+right)//2
        if num_list[mid]==value:
            print("Found!")
            return
        elif num_list[mid]>value:
            right=mid-1
        else:
            left=mid+1
        print(left,right,mid)
    print("Not Found!")
binarysearch(4)

'''

tree_height = [5,7,3,10,11]

def binarysearch(value):
    left = 0 
    right = max(tree_height)
    while left<=right:
        mid=(left+right)//2
        storage=0
        print(left,right,mid)
        for i in tree_height:
            if mid<=i:
                storage=storage+i-mid
        print(storage)
        if storage>=value:
            print("Height is", mid)
            left=mid+1
        else:
            right= mid-1
binarysearch(5)        
            
            

        
            
            













