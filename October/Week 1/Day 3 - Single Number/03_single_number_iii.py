# ============================================================
# Day 3 - VARIANT: Single Number III  (LeetCode 260)
# ============================================================
# The question:
#   Every number appears twice, except TWO numbers that appear once.
#   Return those two (any order). O(n) time, O(1) space.
#
#   Example: [1, 2, 1, 3, 2, 5] -> [3, 5]
#
# The big idea (XOR + split into two groups):
#   1. XOR everything -> you get a ^ b (the two singles mixed together).
#   2. a and b are different, so a ^ b has at least one bit set to 1.
#      That bit is 1 in one of them and 0 in the other.
#   3. Grab the lowest such bit:  diff & -diff
#   4. Split all numbers into two groups by that bit.
#      a goes in one group, b in the other, and every pair stays together.
#   5. XOR each group separately -> each group gives you one single.
# ============================================================


def single_number_iii_brute(nums):
    # Brute force: count with a dict.
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    result = []
    for num in counts:
        if counts[num] == 1:
            result.append(num)
    return result


def single_number_iii(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num              # this is a ^ b

    low_bit = xor_all & -xor_all    # keeps only the lowest 1 bit

    a = 0
    b = 0
    for num in nums:
        if num & low_bit:
            a ^= num                # group where that bit is ON
        else:
            b ^= num                # group where that bit is OFF

    return [a, b]


if __name__ == "__main__":
    print(single_number_iii([1, 2, 1, 3, 2, 5]))   # [3, 5] (any order)
    print(single_number_iii([-1, 0]))              # [-1, 0]
    print(single_number_iii([0, 1]))               # [1, 0]
