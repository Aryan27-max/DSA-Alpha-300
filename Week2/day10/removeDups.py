def RemoveDuplicates(nums): 
    #dealing with null input
    if len(nums) == 0: 
        return 0 

    # locking in index 0 
    write = 1

    for read in range (1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write 

nums = [1,1,2,2,3]
k = RemoveDuplicates(nums)

# this k shows the no. of unique values 
print(k)
#this one displays the actual elements 
print(nums[:k])