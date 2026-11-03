# ============================================================
# Day 30 - VARIANT: Remove Duplicates from Sorted Array  (LeetCode 26)
# ============================================================
# The question:
#   Sorted list. Remove duplicates in place so each value appears once,
#   keeping order. Return k, the number of unique values.
#
#   Example: [0,0,1,1,1,2,2,3,3,4] -> 5, [0,1,2,3,4,...]
#
# Today's angle - ONE template for the whole family:
#   Day 10 solved "at most 1" and "at most 2" separately. Both are the
#   same rule: keep x if fewer than k values have been written, or if x
#   is different from the value k slots back in the written part.
#     k = 1 -> Remove Duplicates (LC 26)
#     k = 2 -> Remove Duplicates II (LC 80)
#   Learn the template once, use it for any k.
# ============================================================


def remove_duplicates_brute(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def keep_at_most(nums, k):
    write = 0
    for x in nums:
        if write < k or nums[write - k] != x:
            nums[write] = x             # still room for this value
            write += 1
    return write


def remove_duplicates(nums):
    return keep_at_most(nums, 1)


if __name__ == "__main__":
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(a)
    print(k, a[:k])       # 5 [0, 1, 2, 3, 4]

    b = [1, 1, 1, 2, 2, 3]
    k = keep_at_most(b, 2)
    print(k, b[:k])       # 5 [1, 1, 2, 2, 3]
