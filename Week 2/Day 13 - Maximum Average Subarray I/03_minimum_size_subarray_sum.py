# ============================================================
# Day 13 - VARIANT: Minimum Size Subarray Sum  (LeetCode 209)
# ============================================================
# The question:
#   All numbers are positive. Find the length of the SHORTEST contiguous
#   subarray whose sum is >= target. Return 0 if there isn't one.
#
#   Example: target = 7, nums = [2,3,1,2,4,3] -> 2  ([4,3])
#
# The big idea (VARIABLE-size window - grow, then shrink):
#   - Move right forward, adding numbers, until the sum reaches target.
#   - Now shrink from the left as much as possible while still >= target,
#     recording the length each time.
#   Every number enters once and leaves once -> O(n).
#   (This only works because numbers are positive - shrinking always
#   lowers the sum.)
# ============================================================


def min_sub_array_len_brute(target, nums):
    # Brute force: from each start, extend until the sum is big enough.
    n = len(nums)
    best = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s >= target:
                length = j - i + 1
                if best == 0 or length < best:
                    best = length
                break
    return best


def min_sub_array_len(target, nums):
    left = 0
    window = 0
    best = len(nums) + 1                    # "infinity" - longer than any real answer

    for right in range(len(nums)):
        window += nums[right]               # grow the window

        while window >= target:             # big enough? try to shrink it
            length = right - left + 1
            if length < best:
                best = length
            window -= nums[left]
            left += 1

    return 0 if best == len(nums) + 1 else best


if __name__ == "__main__":
    print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))           # 2
    print(min_sub_array_len(4, [1, 4, 4]))                    # 1
    print(min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1, 1]))    # 0
