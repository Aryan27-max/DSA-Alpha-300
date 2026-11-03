# ============================================================
# Day 4 - VARIANT: Range Sum Query - Immutable  (LeetCode 303)
# ============================================================
# The question:
#   Build a class NumArray. It gets a list once, then answers many
#   questions: sumRange(left, right) = sum of nums[left..right] inclusive.
#   The list never changes.
#
#   Example: nums = [-2, 0, 3, -5, 2, -1]
#            sumRange(0, 2) -> 1     sumRange(2, 5) -> -1
#
# The big idea:
#   Do the work ONCE up front: build a prefix array where
#   prefix[i] = sum of the first i numbers (prefix[0] = 0).
#   Then any range is just a subtraction:
#       sum(left..right) = prefix[right + 1] - prefix[left]
#   Each query becomes O(1).
# ============================================================


class NumArrayBrute:
    # Brute force: loop through the range on every query.
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total


class NumArray:
    def __init__(self, nums):
        # prefix has one extra slot at the front so we never need special cases
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        # everything up to right, minus everything before left
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))   # 1
    print(obj.sumRange(2, 5))   # -1
    print(obj.sumRange(0, 5))   # -3
