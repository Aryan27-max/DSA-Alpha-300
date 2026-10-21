# ============================================================
# Day 3 - VARIANT: Single Number II  (LeetCode 137)
# ============================================================
# The question:
#   Every number appears exactly THREE times, except one which appears once.
#   Find it with O(n) time and O(1) extra space.
#
#   Example: [0, 1, 0, 1, 0, 1, 99] -> 99
#
# The big idea (count bits):
#   XOR alone won't work (three copies don't cancel).
#   Look at one bit position at a time. Add up that bit across all numbers.
#   Numbers that appear 3 times add 0 or 3 to the total.
#   So total % 3 is exactly the bit of the single number.
#   Do this for all 32 bits and rebuild the number.
#   Last step: if bit 31 is set, the answer is negative (32-bit signed).
# ============================================================


def single_number_ii_brute(nums):
    # Brute force: count each number with a hand-made dict.
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    for num in counts:
        if counts[num] == 1:
            return num
    return None


def single_number_ii(nums):
    result = 0

    for bit in range(32):
        bit_total = 0
        for num in nums:
            bit_total += (num >> bit) & 1   # is this bit switched on in num?

        if bit_total % 3 == 1:
            result |= (1 << bit)            # the single number has this bit on

    # turn it into a negative number if the sign bit (bit 31) is on
    if result >= 2 ** 31:
        result -= 2 ** 32

    return result


if __name__ == "__main__":
    print(single_number_ii([2, 2, 3, 2]))               # 3
    print(single_number_ii([0, 1, 0, 1, 0, 1, 99]))     # 99
    print(single_number_ii([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))   # -4
