# ============================================================
# Day 21 - VARIANT: Range Sum Query - Mutable  (LeetCode 307)
# ============================================================
# The question:
#   Like the primary, but now there's also update(index, val), which
#   changes nums[index]. Support both operations efficiently.
#
#   Example: NumArray([1,3,5])
#            sumRange(0,2) -> 9
#            update(1,2)       (nums becomes [1,2,5])
#            sumRange(0,2) -> 8
#
# Why the primary's trick breaks:
#   A plain prefix array makes queries O(1) but an update O(n) - every
#   prefix after the index has to change.
#
# The big idea (Fenwick tree / Binary Indexed Tree - the segment tree bridge):
#   A list 'tree' (1-indexed) where tree[i] stores the sum of a block of
#   numbers ending at i. The block size is the lowest set bit of i:
#     i & -i   (e.g. 6 = 110b -> block of 2, 8 = 1000b -> block of 8)
#   - prefix_sum(i): add tree[i], then jump i -= i & -i, until 0.
#   - add(i, delta): add delta to tree[i], then jump i += i & -i.
#   Each jump removes or adds one bit, so both are O(log n).
#   Range sum = prefix_sum(right) - prefix_sum(left - 1), same as today's
#   primary.
# ============================================================


class NumArrayBrute:
    # Plain list: update O(1), query O(n).
    def __init__(self, nums):
        self.nums = nums[:]

    def update(self, index, val):
        self.nums[index] = val

    def sumRange(self, left, right):
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total


class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]                 # keep current values so update knows the change
        self.tree = [0] * (self.n + 1)      # index 0 unused (Fenwick trees are 1-indexed)
        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i                     # move to the next block that covers i

    def _prefix_sum(self, i):
        # sum of nums[0 .. i-1] (i is 1-indexed here)
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i                     # drop the lowest set bit
        return total

    def update(self, index, val):
        delta = val - self.nums[index]      # how much it changed by
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left, right):
        return self._prefix_sum(right + 1) - self._prefix_sum(left)


if __name__ == "__main__":
    obj = NumArray([1, 3, 5])
    print(obj.sumRange(0, 2))   # 9
    obj.update(1, 2)
    print(obj.sumRange(0, 2))   # 8
    print(obj.sumRange(1, 1))   # 2
