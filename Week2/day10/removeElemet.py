
def removeElement(nums, val):
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1

    return write


nums = [3, 2, 2, 3]
k = removeElement(nums, 3)
print(nums[:k])  # [2, 2]
