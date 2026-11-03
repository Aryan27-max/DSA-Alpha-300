# ============================================================
# Day 20 - PRIMARY: Find Pivot Index  (LeetCode 724)
# ============================================================
# The question:
#   The pivot index is where the sum of everything to its LEFT equals
#   the sum of everything to its RIGHT (the pivot itself isn't counted).
#   Return the LEFTMOST pivot index, or -1 if none exists.
#   At the edges, the empty side counts as 0.
#
#   Example: [1,7,3,6,5,6] -> 3   (1+7+3 = 11 = 5+6)
#            [2,1,-1] -> 0        (left = 0, right = 1 + -1 = 0)
#
# The big idea (total + running left sum):
#   Get the total once. Walk left to right, carrying left_sum.
#     right_sum = total - left_sum - nums[i]
#   If left_sum == right_sum, that's the pivot.
#   Then add nums[i] to left_sum and move on.
#   (No sum(nums[:i]) inside the loop - that's O(n^2). No accumulate.)
# ============================================================


def pivot_index_brute(nums):
    # Brute force: for each index, add up both sides from scratch.
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


def pivot_index(nums):
    total = 0
    for x in nums:
        total += x

    left_sum = 0
    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]   # everything except the left side and me
        if left_sum == right_sum:
            return i
        left_sum += nums[i]                      # I move into the left side

    return -1


if __name__ == "__main__":
    print(pivot_index([1, 7, 3, 6, 5, 6]))   # 3
    print(pivot_index([1, 2, 3]))            # -1
    print(pivot_index([2, 1, -1]))           # 0
