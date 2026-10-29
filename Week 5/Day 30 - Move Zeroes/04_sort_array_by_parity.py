# ============================================================
# Day 30 - VARIANT: Sort Array By Parity  (LeetCode 905)
# ============================================================
# The question:
#   Put all even numbers before all odd numbers. Any order inside each
#   group is fine.
#
#   Example: [3,1,2,4] -> [4,2,1,3] (or any evens-then-odds order)
#
# Today's angle - pointers from BOTH ends (Day 10 used read/write):
#   left looks for an odd number that's on the wrong side,
#   right looks for an even number that's on the wrong side,
#   swap them. Each swap fixes TWO misplaced numbers at once, so it does
#   at most n/2 swaps. (This is the partition step of quicksort -
#   you'll write that in November.)
# ============================================================


def sort_array_by_parity_brute(nums):
    result = []
    for x in nums:
        if x % 2 == 0:
            result.append(x)
    for x in nums:
        if x % 2 == 1:
            result.append(x)
    return result


def sort_array_by_parity(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1                   # already on the correct side
        elif nums[right] % 2 == 1:
            right -= 1                  # already on the correct side
        else:
            nums[left], nums[right] = nums[right], nums[left]   # odd left, even right: swap
            left += 1
            right -= 1
    return nums


if __name__ == "__main__":
    print(sort_array_by_parity([3, 1, 2, 4]))   # [4, 2, 1, 3]
    print(sort_array_by_parity([0]))            # [0]
    print(sort_array_by_parity([1, 3, 5, 2]))   # [2, 3, 5, 1]
