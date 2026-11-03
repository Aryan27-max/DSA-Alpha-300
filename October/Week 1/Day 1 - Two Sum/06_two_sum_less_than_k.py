# ============================================================
# Day 1 - VARIANT: Two Sum Less Than K  (LeetCode 1099 - Premium)
# ============================================================
# The question:
#   Find the MAXIMUM sum of two different elements that is strictly less than k.
#   If no pair works, return -1.
#
#   Example: nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60  ->  58  (34 + 24)
#
# The big idea:
#   Sort it (our own sort), then two pointers.
#   If the sum is < k, it's a candidate - save it and try a bigger left.
#   If the sum is >= k, it's too big - move right down.
# ============================================================


def merge_sort(arr):
    # Our own merge sort (sorted() is not allowed in October).
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    while i < len(left):
        merged.append(left[i]); i += 1
    while j < len(right):
        merged.append(right[j]); j += 1
    return merged


def two_sum_less_than_k_brute(nums, k):
    # Brute force: check every pair, keep the best one under k.
    best = -1
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            s = nums[i] + nums[j]
            if s < k and s > best:
                best = s
    return best


def two_sum_less_than_k(nums, k):
    nums = merge_sort(nums)
    left, right = 0, len(nums) - 1
    best = -1

    while left < right:
        total = nums[left] + nums[right]
        if total < k:
            if total > best:
                best = total            # valid pair, keep the biggest one
            left += 1                   # try to push the sum higher
        else:
            right -= 1                  # too big, shrink it

    return best


if __name__ == "__main__":
    print(two_sum_less_than_k([34, 23, 1, 24, 75, 33, 54, 8], 60))   # 58
    print(two_sum_less_than_k([10, 20, 30], 15))                     # -1
