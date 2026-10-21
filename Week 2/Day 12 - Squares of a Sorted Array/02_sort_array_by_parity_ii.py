# ============================================================
# Day 12 - VARIANT: Sort Array By Parity II  (LeetCode 922)
# ============================================================
# The question:
#   Half the numbers are even, half are odd. Rearrange so that every even
#   INDEX holds an even number and every odd INDEX holds an odd number.
#
#   Example: [4,2,5,7] -> [4,5,2,7]  (any valid answer is fine)
#
# The big idea (two pointers that hop by 2):
#   even = 0, 2, 4, ...   odd = 1, 3, 5, ...
#   Move 'even' forward until it finds an odd number sitting in an even spot.
#   Move 'odd' forward until it finds an even number sitting in an odd spot.
#   Those two are each other's fix -> swap them.
# ============================================================


def sort_array_by_parity_ii_brute(nums):
    # New list: put evens in even slots and odds in odd slots as we meet them.
    result = [0] * len(nums)
    e, o = 0, 1
    for x in nums:
        if x % 2 == 0:
            result[e] = x
            e += 2
        else:
            result[o] = x
            o += 2
    return result


def sort_array_by_parity_ii(nums):
    n = len(nums)
    odd = 1

    for even in range(0, n, 2):
        if nums[even] % 2 == 1:             # an odd number is in an even slot
            while nums[odd] % 2 == 1:       # find an even number in an odd slot
                odd += 2
            nums[even], nums[odd] = nums[odd], nums[even]

    return nums


if __name__ == "__main__":
    print(sort_array_by_parity_ii([4, 2, 5, 7]))   # [4, 5, 2, 7]
    print(sort_array_by_parity_ii([2, 3]))         # [2, 3]
    print(sort_array_by_parity_ii([3, 1, 4, 2]))   # [2, 1, 4, 3]
