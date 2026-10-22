# ============================================================
# Day 20 - VARIANT: Find the Middle Index in Array  (LeetCode 1991)
# ============================================================
# The question:
#   Return the leftmost middleIndex where
#     nums[0] + ... + nums[middleIndex-1] == nums[middleIndex+1] + ... + nums[n-1]
#   or -1 if there isn't one.
#
#   Example: [2,3,-1,8,4] -> 3   (2+3-1 = 4 = 4)
#
# The big idea:
#   This is the exact same problem as Find Pivot Index (different name,
#   same definition). Writing it again from memory is the point: total,
#   running left sum, right = total - left - nums[i].
#   Small twist for practice: compare 2 * left_sum + nums[i] == total,
#   which is the same equation rearranged.
# ============================================================


def find_middle_index_brute(nums):
    n = len(nums)
    for i in range(n):
        left = 0
        for j in range(i):
            left += nums[j]
        right = 0
        for j in range(i + 1, n):
            right += nums[j]
        if left == right:
            return i
    return -1


def find_middle_index(nums):
    total = 0
    for x in nums:
        total += x

    left_sum = 0
    for i in range(len(nums)):
        # left == right  <=>  left == total - left - nums[i]  <=>  2*left + nums[i] == total
        if 2 * left_sum + nums[i] == total:
            return i
        left_sum += nums[i]

    return -1


if __name__ == "__main__":
    print(find_middle_index([2, 3, -1, 8, 4]))   # 3
    print(find_middle_index([1, -1, 4]))         # 2
    print(find_middle_index([2, 5]))             # -1
