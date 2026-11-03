# ============================================================
# Day 2 - VARIANT: Contains Duplicate II  (LeetCode 219)
# ============================================================
# The question:
#   Return True if there are two DIFFERENT indexes i and j with
#   nums[i] == nums[j] AND the distance |i - j| <= k.
#
#   Example: nums = [1, 2, 3, 1], k = 3  -> True  (index 0 and 3, distance 3)
#            nums = [1, 2, 3, 1, 2, 3], k = 2 -> False
#
# The big idea:
#   Remember the LAST index where we saw each number (dict).
#   When we see a number again, check how far back its last copy was.
# ============================================================


def contains_nearby_duplicate_brute(nums, k):
    # Brute force: for each i, look at most k steps ahead.
    n = len(nums)
    for i in range(n):
        j = i + 1
        while j < n and j - i <= k:
            if nums[i] == nums[j]:
                return True
            j += 1
    return False


def contains_nearby_duplicate(nums, k):
    last_seen = {}                      # number -> most recent index

    for i in range(len(nums)):
        num = nums[i]
        if num in last_seen and i - last_seen[num] <= k:
            return True                 # same number, close enough
        last_seen[num] = i              # update to the newest position

    return False


if __name__ == "__main__":
    print(contains_nearby_duplicate([1, 2, 3, 1], 3))          # True
    print(contains_nearby_duplicate([1, 0, 1, 1], 1))          # True
    print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))    # False
