# ============================================================
# Day 10 - VARIANT: Remove Element  (LeetCode 27)
# ============================================================
# The question:
#   Remove every occurrence of val from nums IN PLACE. Return k = how many
#   elements are left. The first k slots hold them (order doesn't matter).
#
#   Example: nums = [3,2,2,3], val = 3 -> k = 2, first two = [2,2]
#
# The big idea (read/write again):
#   Copy every element that is NOT val to nums[write].
# ============================================================


def remove_element_brute(nums, val):
    # Pop every match (each pop shifts the rest left).
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def remove_element(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]    # keep everything that isn't val
            write += 1
    return write


if __name__ == "__main__":
    a = [3, 2, 2, 3]
    k = remove_element(a, 3)
    print(k, a[:k])     # 2 [2, 2]

    b = [0, 1, 2, 2, 3, 0, 4, 2]
    k = remove_element(b, 2)
    print(k, b[:k])     # 5 [0, 1, 3, 0, 4]
