# ============================================================
# Day 10 - VARIANT: Sort Array By Parity  (LeetCode 905)
# ============================================================
# The question:
#   Move all even numbers to the front and all odd numbers to the back.
#   Any order inside each group is fine.
#
#   Example: [3,1,2,4] -> [2,4,3,1]  (or [4,2,1,3], etc.)
#
# The big idea:
#   Exactly Move Zeroes, with a different test: "is it even?"
#   Every even number gets swapped forward to the write pointer.
# ============================================================


def sort_array_by_parity_brute(nums):
    # Two passes into a new list: evens first, then odds.
    result = []
    for x in nums:
        if x % 2 == 0:
            result.append(x)
    for x in nums:
        if x % 2 == 1:
            result.append(x)
    return result


def sort_array_by_parity(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] % 2 == 0:
            nums[write], nums[read] = nums[read], nums[write]   # even goes to the front
            write += 1
    return nums


if __name__ == "__main__":
    print(sort_array_by_parity([3, 1, 2, 4]))   # [2, 4, 3, 1]
    print(sort_array_by_parity([0]))            # [0]
