# ============================================================
# Day 20 - VARIANT: Running Sum of 1d Array  (LeetCode 1480)
# ============================================================
# The question:
#   runningSum[i] = nums[0] + nums[1] + ... + nums[i]. Return it.
#
#   Example: [1,2,3,4] -> [1,3,6,10]
#
# The big idea (the prerequisite for everything today):
#   Carry the total forward. Every pivot-style problem is built on this:
#   the "left sum" at index i is just runningSum[i - 1].
#   Done in place here: nums[i] += nums[i - 1].
# ============================================================


def running_sum_brute(nums):
    # Brute force: re-add from the start for every position.
    result = []
    for i in range(len(nums)):
        s = 0
        for j in range(i + 1):
            s += nums[j]
        result.append(s)
    return result


def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]          # previous slot already holds the sum so far
    return nums


if __name__ == "__main__":
    print(running_sum([1, 2, 3, 4]))           # [1, 3, 6, 10]
    print(running_sum([1, 1, 1, 1, 1]))        # [1, 2, 3, 4, 5]
    print(running_sum_brute([3, 1, 2, 10, 1])) # [3, 4, 6, 16, 17]
