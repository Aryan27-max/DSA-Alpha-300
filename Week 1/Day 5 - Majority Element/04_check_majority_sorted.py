# ============================================================
# Day 5 - VARIANT: Check If a Number Is Majority Element in a Sorted Array
#                  (LeetCode 1150 - Premium)
# ============================================================
# The question:
#   Sorted array nums and a number target. Return True if target
#   appears MORE than n / 2 times.
#
#   Example: nums = [2, 4, 5, 5, 5, 5, 5, 6, 6], target = 5 -> True
#
# The big idea:
#   Find the FIRST position of target with binary search (call it i).
#   If target is the majority, its block is longer than n/2,
#   so position i + n//2 must still be target.
#   One binary search + one check = O(log n).
# ============================================================


def is_majority_brute(nums, target):
    # Brute force: count it.
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count > len(nums) // 2


def lower_bound(nums, target):
    # Our own binary search: first index where nums[index] >= target.
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def is_majority_element(nums, target):
    n = len(nums)
    start = lower_bound(nums, target)
    end_check = start + n // 2              # where the block must still reach

    return end_check < n and nums[end_check] == target


if __name__ == "__main__":
    print(is_majority_element([2, 4, 5, 5, 5, 5, 5, 6, 6], 5))   # True
    print(is_majority_element([10, 100, 101, 101], 101))         # False
    print(is_majority_element([1, 1, 2], 1))                     # True
