def merge_sort(l,r, original_list):
    if l==r:
        return
    print(l,r)
    mid=(l+r)//2
    merge_sort(l,mid,original_list)
    merge_sort(mid+1,r,original_list)
    print('before',original_list)
    merge(l,r,mid,original_list)
    print('after', original_list)
    
def merge(l,r,mid, original_list):
    left_list = [original_list[i] for i in range(l,mid+1)]
    right_list =[original_list[i]for i in range(mid+1,r+1)]
    
    i=0 
    j=0
    k=l
    while i!=len(left_list)and j!=len(right_list):
        if left_list[i]>right_list[j]:
            original_list[k]=right_list[j]
            j=j+1
        else:
            original_list[k]=left_list[i]
            i=i+1
        k=k+1
    while i!=len(left_list):
        original_list[k]=left_list[i]
        i=i+1
        k=k+1
    while j!=len(right_list):
        original_list[k]=right_list[j]
        j=j+1
        k=k+1
numbers=[7,4,1,5,9,2]
merge_sort(0,5,numbers)       
        
        
