# ============================================================
# Day 20 - VARIANT: Minimum Value to Get Positive Step by Step Sum  (LeetCode 1413)
# ============================================================
# The question:
#   Pick a positive starting value startValue. Walk through nums adding
#   each number to it. The running total must stay >= 1 the whole time.
#   Return the smallest startValue that works.
#
#   Example: [-3,2,-3,4,2] -> 5
#            running sums with 5: 2, 4, 1, 5, 7 (never below 1)
#
# The big idea (minimum prefix sum):
#   Walk the prefix sums starting from 0. Track the LOWEST point.
#   startValue + lowest must be >= 1, so startValue = 1 - lowest.
#   If the lowest point is never below 0, startValue = 1.
# ============================================================


def min_start_value_brute(nums):
    # Brute force: try 1, 2, 3, ... until one works.
    start = 1
    while True:
        total = start
        ok = True
        for x in nums:
            total += x
            if total < 1:
                ok = False
                break
        if ok:
            return start
        start += 1


def min_start_value(nums):
    prefix = 0
    lowest = 0                          # the starting point (before any steps) counts as 0
    for x in nums:
        prefix += x
        if prefix < lowest:
            lowest = prefix             # deepest dip so far

    return 1 - lowest                   # lift the deepest dip up to exactly 1


if __name__ == "__main__":
    print(min_start_value([-3, 2, -3, 4, 2]))   # 5
    print(min_start_value([1, 2]))              # 1
    print(min_start_value([1, -2, -3]))         # 5
