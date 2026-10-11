
def removeDuplicatesTwice(nums):
    if len(nums) <= 2:
        return len(nums)

    write = 2

    for read in range(2, len(nums)):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write


nums = [1, 1, 1, 2, 2, 3]
k = removeDuplicatesTwice(nums)
print(nums[:k])  # [1, 1, 2, 2, 3]
