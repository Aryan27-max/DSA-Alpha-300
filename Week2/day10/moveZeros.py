
def moveZeroes(nums):
    write = 0

    # Pack all nonzero values toward the front.
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    # Fill the leftover positions with zeroes.
    while write < len(nums):
        nums[write] = 0
        write += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # [1, 3, 12, 0, 0]
