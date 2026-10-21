# ============================================================
# Day 14 - PRIMARY: Contains Duplicate II  (LeetCode 219)
# ============================================================
# The question:
#   Return True if there are two different indexes i and j with
#   nums[i] == nums[j] and |i - j| <= k.
#
#   Example: nums = [1,2,3,1], k = 3 -> True
#            nums = [1,2,3,1,2,3], k = 2 -> False
#
# Week 1 vs Week 2:
#   On Day 2 you solved this with a last-seen-index dict. Today, look at
#   it as a SLIDING WINDOW: "Is the current number already inside the
#   window of the last k numbers?"
#
#   Two ways to keep that window:
#   A) Rolling dict of last-seen index (update it inline every step).
#   B) A set that holds exactly the last k values: add the new one,
#      remove the one that just slid out (nums[i - k]).
#   Both are O(n). The set version keeps memory at O(k) instead of O(n).
# ============================================================


def contains_nearby_duplicate_brute(nums, k):
    # Brute force: compare each number with the next k numbers.
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_nearby_duplicate_dict(nums, k):
    # A) rolling dict: value -> most recent index
    last_seen = {}
    for i in range(len(nums)):
        if nums[i] in last_seen and i - last_seen[nums[i]] <= k:
            return True
        last_seen[nums[i]] = i              # overwrite with the newest position
    return False


def contains_nearby_duplicate(nums, k):
    # B) sliding window set: only the last k values live in here
    window = set()
    for i in range(len(nums)):
        if nums[i] in window:
            return True                     # duplicate within distance k
        window.add(nums[i])
        if len(window) > k:
            window.discard(nums[i - k])     # oldest value slides out
    return False


if __name__ == "__main__":
    print(contains_nearby_duplicate([1, 2, 3, 1], 3))            # True
    print(contains_nearby_duplicate([1, 0, 1, 1], 1))            # True
    print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))      # False
    print(contains_nearby_duplicate_dict([1, 2, 3, 1], 3))       # True
