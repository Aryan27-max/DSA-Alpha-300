# ============================================================
# Day 1 - PRIMARY: Two Sum  (LeetCode 1)
# ============================================================
# The question:
#   You get a list of numbers and a target. Find the two positions
#   whose numbers add up to the target, and return those two indexes.
#   There is exactly one answer, and you can't use the same element twice.
#
#   Example: nums = [2, 7, 11, 15], target = 9  ->  [0, 1]  (2 + 7 = 9)
#
# The big idea:
#   For every number x, the partner we need is (target - x).
#   If we remember every number we've already walked past (in a dict),
#   we can check "have I seen my partner?" in O(1).
# ============================================================


def two_sum_brute(nums, target):
    # Brute force: try every possible pair. Simple, but slow.
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):          # j starts after i so we never reuse an element
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums, target):
    # Optimal: one pass with a hand-made dict.
    seen = {}                               # number -> the index where we saw it

    for i in range(len(nums)):
        need = target - nums[i]             # the partner that would complete the pair

        if need in seen:                    # partner already walked past? done!
            return [seen[need], i]

        seen[nums[i]] = i                   # otherwise remember this number for later

    return []                               # problem promises an answer, but just in case


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))       # [0, 1]
    print(two_sum([3, 2, 4], 6))            # [1, 2]
    print(two_sum([3, 3], 6))               # [0, 1]
    print(two_sum_brute([3, 2, 4], 6))      # [1, 2]
