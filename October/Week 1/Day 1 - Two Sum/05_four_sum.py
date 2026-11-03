# ============================================================
# Day 1 - VARIANT: 4Sum  (LeetCode 18)
# ============================================================
# The question:
#   Return all UNIQUE quadruplets [a, b, c, d] such that a + b + c + d == target.
#
#   Example: nums = [1, 0, -1, 0, -2, 2], target = 0
#            -> [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
#
# The big idea:
#   It's 3Sum with one more loop. Sort, fix TWO numbers (i and j),
#   then use two pointers for the last two. Skip duplicates at every level.
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


def four_sum_brute(nums, target):
    # Brute force: 4 nested loops, set of tuples to remove repeats. O(n^4).
    nums = merge_sort(nums)
    n = len(nums)
    found = set()
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        found.add((nums[a], nums[b], nums[c], nums[d]))
    return [list(t) for t in found]


def four_sum(nums, target):
    nums = merge_sort(nums)
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                                    # skip repeated first number

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue                                # skip repeated second number

            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


if __name__ == "__main__":
    print(four_sum([1, 0, -1, 0, -2, 2], 0))   # [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
    print(four_sum([2, 2, 2, 2, 2], 8))        # [[2, 2, 2, 2]]
