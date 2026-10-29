# ============================================================
# Day 30 - VARIANT: Remove Element  (LeetCode 27)
# ============================================================
# The question:
#   Remove every val from nums in place and return k, the number left.
#   The first k slots must hold the kept values (ORDER DOESN'T MATTER).
#
#   Example: nums = [3,2,2,3], val = 3 -> k = 2, nums starts with [2,2]
#
# Today's angle (Day 10 did read/write):
#   Because order doesn't matter, there's a trick that writes less when
#   val is rare: when nums[i] == val, overwrite it with the LAST element
#   and shrink the array by one. Don't move i - the value we just pulled
#   in still needs checking.
#   read/write  : one write per KEPT element
#   swap-to-end : one write per REMOVED element
# ============================================================


def remove_element_brute(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)                 # shifts everything after i
        else:
            i += 1
    return len(nums)


def remove_element_read_write(nums, val):
    write = 0
    for x in nums:
        if x != val:
            nums[write] = x
            write += 1
    return write


def remove_element(nums, val):
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]       # pull in the last element
            n -= 1                      # the array is one shorter now
        else:
            i += 1
    return n


if __name__ == "__main__":
    a = [3, 2, 2, 3]
    k = remove_element(a, 3)
    print(k, a[:k])       # 2 [2, 2]

    b = [0, 1, 2, 2, 3, 0, 4, 2]
    k = remove_element(b, 2)
    print(k, b[:k])       # 5 [0, 1, 4, 0, 3]  (any order)
