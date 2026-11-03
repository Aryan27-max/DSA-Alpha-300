# ============================================================
# Day 21 - PRIMARY: Range Sum Query - Immutable  (LeetCode 303)
# ============================================================
# The question:
#   Build a class NumArray(nums). It must answer many calls of
#   sumRange(left, right) = nums[left] + ... + nums[right] (inclusive).
#   nums never changes.
#
#   Example: nums = [-2, 0, 3, -5, 2, -1]
#            sumRange(0, 2) -> 1
#            sumRange(2, 5) -> -1
#            sumRange(0, 5) -> -3
#
# The big idea (build once, query many):
#   Do the adding ONCE in __init__:
#     prefix[0] = 0
#     prefix[i + 1] = prefix[i] + nums[i]       (sum of the first i+1 numbers)
#   Then any range is one subtraction:
#     sumRange(l, r) = prefix[r + 1] - prefix[l]
#   Build: O(n). Each query: O(1). With q queries that's O(n + q) instead
#   of O(n * q) - precomputing pays off as soon as you ask more than once.
#   (No itertools.accumulate - build it with a loop.)
# ============================================================


class NumArrayBrute:
    # Brute force: loop over the range on every query.
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total


class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)     # the extra leading 0 removes edge cases
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        # (sum of nums[0..right]) - (sum of nums[0..left-1])
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))   # 1
    print(obj.sumRange(2, 5))   # -1
    print(obj.sumRange(0, 5))   # -3
