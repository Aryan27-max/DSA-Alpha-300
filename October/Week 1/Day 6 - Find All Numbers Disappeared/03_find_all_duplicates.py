# ============================================================
# Day 6 - VARIANT: Find All Duplicates in an Array  (LeetCode 442)
# ============================================================
# The question:
#   n numbers, each in 1..n, each appears once or twice.
#   Return every number that appears twice. O(n) time, O(1) space.
#
#   Example: [4, 3, 2, 7, 8, 2, 3, 1] -> [2, 3]
#
# The big idea (cyclic sort - a different in-place trick from Day 2):
#   Day 2 solved this with negative marking. Here's another way:
#   Try to put every number v into its home index v - 1 by swapping.
#   After that, any index i where nums[i] != i + 1 is holding a
#   number that couldn't go home because its home was already taken
#   -> that number is a duplicate.
# ============================================================


def find_duplicates_brute(nums):
    # Set version: O(n) space.
    seen = set()
    dups = []
    for num in nums:
        if num in seen:
            dups.append(num)
        else:
            seen.add(num)
    return dups


def find_duplicates(nums):
    i = 0
    n = len(nums)

    # Step 1: send every number to its home (cyclic sort)
    while i < n:
        home = nums[i] - 1
        if nums[i] != nums[home]:
            nums[i], nums[home] = nums[home], nums[i]   # swap it home, check new nums[i]
        else:
            i += 1          # already home, or home has a copy -> move on

    # Step 2: anyone not sitting at home is an extra copy
    dups = []
    for i in range(n):
        if nums[i] != i + 1:
            dups.append(nums[i])
    return dups


if __name__ == "__main__":
    print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))   # [3, 2] (any order)
    print(find_duplicates([1, 1, 2]))                  # [1]
