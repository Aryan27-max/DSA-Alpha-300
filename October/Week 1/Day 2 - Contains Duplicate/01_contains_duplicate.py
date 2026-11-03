# ============================================================
# Day 2 - PRIMARY: Contains Duplicate  (LeetCode 217)
# ============================================================
# The question:
#   Return True if any value appears at least twice in the list,
#   and False if every element is different.
#
#   Example: [1, 2, 3, 1] -> True     [1, 2, 3, 4] -> False
#
# The big idea:
#   Keep a set of numbers we've seen. Before adding a number, ask
#   "have I seen this?" The moment the answer is yes, stop - we're done.
#   (We do NOT use the len(set(nums)) one-liner, because that always
#   reads the whole list even if the duplicate is right at the start.)
# ============================================================


def contains_duplicate_brute(nums):
    # Brute force: compare every pair.
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True         # short-circuit: found the first duplicate, stop right here
        seen.add(num)           # first time seeing it, remember it

    return False                # walked the whole list, everything was unique


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))                    # True
    print(contains_duplicate([1, 2, 3, 4]))                    # False
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
