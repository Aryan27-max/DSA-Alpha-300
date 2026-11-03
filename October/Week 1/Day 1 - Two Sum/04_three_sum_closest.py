# ============================================================
# Day 1 - VARIANT: 3Sum Closest  (LeetCode 16)
# ============================================================
# The question:
#   Pick three numbers whose sum is as close as possible to target.
#   Return that sum (not the numbers). There is exactly one best answer.
#
#   Example: nums = [-1, 2, 1, -4], target = 1  ->  2   (-1 + 2 + 1 = 2)
#
# The big idea:
#   Same skeleton as 3Sum: sort, fix one number, two pointers for the rest.
#   Instead of looking for an exact match, we keep track of the
#   closest sum we've seen so far.
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


def three_sum_closest_brute(nums, target):
    # Brute force: check all triplets and keep the closest.
    n = len(nums)
    best = nums[0] + nums[1] + nums[2]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(best - target):
                    best = s
    return best


def three_sum_closest(nums, target):
    nums = merge_sort(nums)
    n = len(nums)
    best = nums[0] + nums[1] + nums[2]      # any valid triplet is a fine starting guess

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(total - target) < abs(best - target):
                best = total                # found something closer, remember it

            if total == target:
                return total                # can't get closer than exact
            elif total < target:
                left += 1                   # too small -> grab a bigger number
            else:
                right -= 1                  # too big -> grab a smaller number

    return best


if __name__ == "__main__":
    print(three_sum_closest([-1, 2, 1, -4], 1))   # 2
    print(three_sum_closest([0, 0, 0], 1))        # 0
