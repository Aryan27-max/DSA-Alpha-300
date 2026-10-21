# ============================================================
# Day 4 - PRIMARY: Running Sum of 1d Array  (LeetCode 1480)
# ============================================================
# The question:
#   Return a list where each position i holds the sum of
#   nums[0] + nums[1] + ... + nums[i].
#
#   Example: [1, 2, 3, 4] -> [1, 3, 6, 10]
#
# The big idea (prefix sum):
#   Don't re-add everything from scratch each time.
#   running[i] = running[i - 1] + nums[i]
#   Just carry a total forward as you walk. (No itertools.accumulate!)
# ============================================================


def running_sum_brute(nums):
    # Brute force: for each i, add up everything from 0 to i again.
    result = []
    for i in range(len(nums)):
        total = 0
        for j in range(i + 1):
            total += nums[j]
        result.append(total)
    return result


def running_sum(nums):
    result = []
    total = 0
    for num in nums:
        total += num            # carry the total forward
        result.append(total)
    return result


def running_sum_in_place(nums):
    # Same idea, but reuse the input list - O(1) extra space.
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


if __name__ == "__main__":
    print(running_sum([1, 2, 3, 4]))            # [1, 3, 6, 10]
    print(running_sum([1, 1, 1, 1, 1]))         # [1, 2, 3, 4, 5]
    print(running_sum_in_place([3, 1, 2, 10, 1]))  # [3, 4, 6, 16, 17]
