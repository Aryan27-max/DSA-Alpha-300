# ============================================================
# Day 1 - VARIANT: 3Sum  (LeetCode 15)
# ============================================================
# The question:
#   Find all UNIQUE triplets [a, b, c] in the list where a + b + c == 0.
#   The same triplet must not show up twice in the answer.
#
#   Example: [-1, 0, 1, 2, -1, -4]  ->  [[-1, -1, 2], [-1, 0, 1]]
#
# The big idea:
#   1. Sort the array (we write our OWN merge sort - sorted() is banned in October).
#   2. Fix one number nums[i]. Now we need two numbers that sum to -nums[i].
#      That's just Two Sum II on the rest of the array -> two pointers.
#   3. Skip repeated values so we don't produce duplicate triplets.
# ============================================================


def merge_sort(arr):
    # Our own sort: split in half, sort each half, merge them back together.
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # one side may still have leftovers - they're already sorted, just add them
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


def three_sum_brute(nums):
    # Brute force: try every triplet, store a sorted tuple in a set to remove repeats.
    nums = merge_sort(nums)
    n = len(nums)
    found = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    found.add((nums[i], nums[j], nums[k]))
    result = []
    for t in found:
        result.append(list(t))
    return result


def three_sum(nums):
    nums = merge_sort(nums)
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                        # same fixed number as before -> same triplets, skip

        if nums[i] > 0:
            break                           # smallest number is positive, nothing can sum to 0

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # jump past duplicates on both sides
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))    # [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 1, 1]))                # []
    print(three_sum([0, 0, 0]))                # [[0, 0, 0]]
