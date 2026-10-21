# ============================================================
# Day 13 - VARIANT: Max Consecutive Ones III  (LeetCode 1004)
# ============================================================
# The question:
#   Binary list nums and an integer k. You may flip at most k zeros to 1.
#   Return the longest run of consecutive 1s you can get.
#
#   Example: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 -> 6
#
# The big idea (variable window with a "budget"):
#   Rephrase: find the longest window that contains at most k zeros.
#   Grow right; count zeros. If zeros > k, shrink from the left until
#   we're back within budget. Track the biggest window.
# ============================================================


def longest_ones_brute(nums, k):
    # Brute force: from each start, extend until zeros exceed k.
    best = 0
    n = len(nums)
    for i in range(n):
        zeros = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            if zeros > k:
                break
            if j - i + 1 > best:
                best = j - i + 1
    return best


def longest_ones(nums, k):
    left = 0
    zeros = 0
    best = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1                  # we'd have to flip this one

        while zeros > k:                # over budget -> shrink from the left
            if nums[left] == 0:
                zeros -= 1
            left += 1

        if right - left + 1 > best:
            best = right - left + 1

    return best


if __name__ == "__main__":
    print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))                       # 6
    print(longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # 10
