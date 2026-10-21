# ============================================================
# Day 6 - VARIANT: First Missing Positive  (LeetCode 41 - Hard)
# ============================================================
# The question:
#   Unsorted list (can have negatives, zeros, huge numbers, duplicates).
#   Return the SMALLEST positive integer that's not in the list.
#   Must be O(n) time and O(1) extra space.
#
#   Example: [3, 4, -1, 1] -> 2      [7, 8, 9, 11, 12] -> 1
#
# The big idea (cyclic sort):
#   The answer is always somewhere in 1..n+1.
#   (If 1..n are all there, the answer is n+1.)
#   So we only care about values 1..n. Put each one at its home index v - 1.
#   Ignore anything <= 0 or > n - it can't affect the answer.
#   Then walk: the first index i where nums[i] != i + 1 gives answer i + 1.
# ============================================================


def first_missing_positive_brute(nums):
    # Set version: O(n) space.
    present = set()
    for num in nums:
        present.add(num)
    candidate = 1
    while candidate in present:
        candidate += 1
    return candidate


def first_missing_positive(nums):
    n = len(nums)
    i = 0

    while i < n:
        v = nums[i]
        # only swap if v is in range AND its home doesn't already hold v
        if 1 <= v <= n and nums[v - 1] != v:
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1        # first home that's empty

    return n + 1                # 1..n all present


if __name__ == "__main__":
    print(first_missing_positive([1, 2, 0]))            # 3
    print(first_missing_positive([3, 4, -1, 1]))        # 2
    print(first_missing_positive([7, 8, 9, 11, 12]))    # 1
