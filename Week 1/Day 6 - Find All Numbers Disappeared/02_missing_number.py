# ============================================================
# Day 6 - VARIANT: Missing Number  (LeetCode 268)
# ============================================================
# The question:
#   n distinct numbers from the range 0..n. One is missing. Find it
#   using O(1) extra space.
#
#   Example: [3, 0, 1] -> 2
#
# The big idea (math this time - Day 3 used XOR):
#   The sum of 0..n is n * (n + 1) / 2.
#   Subtract what's actually there. The leftover is the missing number.
# ============================================================


def missing_number_brute(nums):
    # Set version: O(n) space.
    present = set()
    for num in nums:
        present.add(num)
    for v in range(len(nums) + 1):
        if v not in present:
            return v
    return -1


def missing_number(nums):
    n = len(nums)
    expected = n * (n + 1) // 2     # what the sum WOULD be with nothing missing

    actual = 0
    for num in nums:
        actual += num

    return expected - actual


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))                    # 2
    print(missing_number([0, 1]))                       # 2
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
