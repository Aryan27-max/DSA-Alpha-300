# ============================================================
# Day 3 - VARIANT: Missing Number  (LeetCode 268)
# ============================================================
# The question:
#   The list has n distinct numbers taken from 0, 1, 2, ..., n.
#   Exactly one number in that range is missing. Find it.
#
#   Example: [3, 0, 1] -> 2
#
# The big idea (XOR):
#   XOR all the indexes 0..n together with all the values.
#   Every number that's present appears twice (once as an index,
#   once as a value) and cancels out. The missing one appears once.
#
#   (The other neat way: n*(n+1)/2 - sum(nums). Both are O(1) space.)
# ============================================================


def missing_number_brute(nums):
    # Brute force: for each candidate 0..n, check if it's in the list.
    n = len(nums)
    for candidate in range(n + 1):
        found = False
        for num in nums:
            if num == candidate:
                found = True
                break
        if not found:
            return candidate
    return -1


def missing_number(nums):
    n = len(nums)
    result = n                  # start with n because indexes only go 0..n-1

    for i in range(n):
        result ^= i             # XOR in the index
        result ^= nums[i]       # XOR in the value

    return result               # all pairs cancelled, only the missing number is left


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))                    # 2
    print(missing_number([0, 1]))                       # 2
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
