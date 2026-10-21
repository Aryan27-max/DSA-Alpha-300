# ============================================================
# Day 1 - VARIANT: Two Sum II - Input Array Is Sorted  (LeetCode 167)
# ============================================================
# The question:
#   Same as Two Sum, but the array is already sorted in increasing order.
#   Return the two positions as 1-based indexes. You must use O(1) extra space.
#
#   Example: numbers = [2, 7, 11, 15], target = 9  ->  [1, 2]
#
# The big idea:
#   Because it's sorted, put one pointer at the start and one at the end.
#   Sum too small? move left pointer right (bigger number).
#   Sum too big?   move right pointer left (smaller number).
#   No dict needed - the sorting does the work for us.
# ============================================================


def two_sum_sorted_brute(numbers, target):
    # Brute force: check every pair.
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []


def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]    # +1 because the answer is 1-indexed
        elif total < target:
            left += 1                       # need a bigger sum -> move left up
        else:
            right -= 1                      # need a smaller sum -> move right down

    return []


if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))   # [1, 2]
    print(two_sum_sorted([2, 3, 4], 6))        # [1, 3]
    print(two_sum_sorted([-1, 0], -1))         # [1, 2]
