# ============================================================
# Day 6 - PRIMARY: Find All Numbers Disappeared in an Array  (LeetCode 448)
# ============================================================
# The question:
#   nums has n numbers, each between 1 and n. Some numbers show up
#   twice, so some others are missing. Return all the missing ones.
#   Follow-up: O(n) time and no extra space (output doesn't count).
#
#   Example: [4, 3, 2, 7, 8, 2, 3, 1] -> [5, 6]
#
# The big idea (use the array as its own hashmap):
#   Each value v has a "home" at index v - 1.
#   Pass 1: for each value, make nums[home] negative -> "v exists".
#   Pass 2: any index that is still positive means nobody marked it,
#           so the number (index + 1) is missing.
#   We use abs() when reading, because a slot may already be negative.
# ============================================================


def find_disappeared_brute(nums):
    # Easy version: put everything in a set, then check 1..n. O(n) space.
    present = set()
    for num in nums:
        present.add(num)
    missing = []
    for v in range(1, len(nums) + 1):
        if v not in present:
            missing.append(v)
    return missing


def find_disappeared_numbers(nums):
    # Pass 1: mark every value's home as "seen" by making it negative
    for i in range(len(nums)):
        home = abs(nums[i]) - 1
        if nums[home] > 0:
            nums[home] = -nums[home]

    # Pass 2: positive slots were never marked -> those numbers are missing
    missing = []
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i + 1)

    return missing


if __name__ == "__main__":
    print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))   # [5, 6]
    print(find_disappeared_numbers([1, 1]))                     # [2]
