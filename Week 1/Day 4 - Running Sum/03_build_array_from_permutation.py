# ============================================================
# Day 4 - VARIANT: Build Array from Permutation  (LeetCode 1920)
# ============================================================
# The question:
#   nums is a permutation of 0..n-1. Build ans where ans[i] = nums[nums[i]].
#   Follow-up: can you do it with O(1) extra space?
#
#   Example: [0, 2, 1, 5, 3, 4] -> [0, 1, 2, 4, 5, 3]
#
# The big idea:
#   The easy way is just a new list.
#   The O(1) space trick: every value is < n, so we can store TWO numbers
#   in one slot:  slot = old + n * new
#     old = slot % n      new = slot // n
#   Pass 1: pack the new value into every slot.
#   Pass 2: divide by n to keep only the new value.
# ============================================================


def build_array(nums):
    # Simple version: new list. O(n) space.
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans


def build_array_in_place(nums):
    n = len(nums)

    # Pass 1: add the new value on top of the old one.
    # We use % n to read the ORIGINAL value, even if that slot was already changed.
    for i in range(n):
        nums[i] += n * (nums[nums[i]] % n)

    # Pass 2: throw away the old value, keep only the new one.
    for i in range(n):
        nums[i] //= n

    return nums


if __name__ == "__main__":
    print(build_array([0, 2, 1, 5, 3, 4]))           # [0, 1, 2, 4, 5, 3]
    print(build_array_in_place([5, 0, 1, 2, 3, 4])) # [4, 5, 0, 1, 2, 3]
