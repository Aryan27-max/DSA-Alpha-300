# ============================================================
# Day 3 - VARIANT: Single Element in a Sorted Array  (LeetCode 540)
# ============================================================
# The question:
#   Sorted array. Every element appears exactly twice except one.
#   Find it in O(log n) time and O(1) space.
#
#   Example: [1, 1, 2, 3, 3, 4, 4, 8, 8] -> 2
#
# The big idea (binary search on pairs):
#   Before the single element, pairs start at EVEN indexes: (0,1), (2,3)...
#   After the single element, everything shifts by one, so pairs start at ODD.
#   So: look at an even index mid.
#     - If nums[mid] == nums[mid + 1], the pairing is still "normal" ->
#       the single element is to the RIGHT.
#     - Otherwise the pairing is already broken -> it's at mid or to the LEFT.
#   (XOR would also work, but it's O(n) - the sorted order lets us do better.)
# ============================================================


def single_non_duplicate_brute(nums):
    # Linear: XOR everything. O(n).
    result = 0
    for num in nums:
        result ^= num
    return result


def single_non_duplicate(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1                    # always look at the start of a pair (even index)

        if nums[mid] == nums[mid + 1]:
            left = mid + 2              # this pair is fine, single is further right
        else:
            right = mid                 # pairing is broken here or earlier

    return nums[left]


if __name__ == "__main__":
    print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))   # 2
    print(single_non_duplicate([3, 3, 7, 7, 10, 11, 11]))      # 10
    print(single_non_duplicate([1]))                           # 1
