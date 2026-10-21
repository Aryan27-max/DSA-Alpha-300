# ============================================================
# Day 12 - VARIANT: Shortest Unsorted Continuous Subarray  (LeetCode 581)
# ============================================================
# The question:
#   Find the shortest piece of the array that, if you sorted ONLY that
#   piece, would make the whole array sorted. Return its length.
#
#   Example: [2,6,4,8,10,9,15] -> 5  (sort [6,4,8,10,9])
#            [1,2,3,4] -> 0
#
# The big idea (two sweeps, no sorting):
#   - Left to right, track the max so far. Any number SMALLER than the max
#     before it is out of place -> the last such index is the right edge.
#   - Right to left, track the min so far. Any number BIGGER than the min
#     after it is out of place -> the last such index is the left edge.
# ============================================================


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    while i < len(left):
        out.append(left[i]); i += 1
    while j < len(right):
        out.append(right[j]); j += 1
    return out


def find_unsorted_subarray_brute(nums):
    # Sort a copy (our own sort), then find the first and last positions that differ.
    s = merge_sort(nums)
    start, end = len(nums), -1
    for i in range(len(nums)):
        if nums[i] != s[i]:
            if i < start:
                start = i
            end = i
    return end - start + 1 if end != -1 else 0


def find_unsorted_subarray(nums):
    n = len(nums)
    right_edge = -1
    biggest = nums[0]
    for i in range(n):
        if nums[i] < biggest:
            right_edge = i              # smaller than something before it -> out of place
        else:
            biggest = nums[i]

    left_edge = 0
    smallest = nums[n - 1]
    for i in range(n - 1, -1, -1):
        if nums[i] > smallest:
            left_edge = i               # bigger than something after it -> out of place
        else:
            smallest = nums[i]

    if right_edge == -1:
        return 0                        # already sorted
    return right_edge - left_edge + 1


if __name__ == "__main__":
    print(find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]))        # 5
    print(find_unsorted_subarray([1, 2, 3, 4]))                   # 0
    print(find_unsorted_subarray([1]))                            # 0
    print(find_unsorted_subarray_brute([2, 6, 4, 8, 10, 9, 15]))  # 5
