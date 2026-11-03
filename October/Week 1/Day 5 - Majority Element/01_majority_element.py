# ============================================================
# Day 5 - PRIMARY: Majority Element  (LeetCode 169)
# ============================================================
# The question:
#   Return the element that appears MORE than n / 2 times.
#   It is guaranteed to exist.
#
#   Example: [2, 2, 1, 1, 1, 2, 2] -> 2
#
# Two solutions (you need both today):
#
#   A) Hashmap counting - O(n) time, O(n) space.
#      Count everything, return the one whose count passes n/2.
#
#   B) Boyer-Moore voting - O(n) time, O(1) space.
#      Imagine a fight: each element either supports the current
#      candidate (+1) or attacks it (-1). When the count hits 0,
#      the next element becomes the new candidate.
#      The majority has more soldiers than everyone else combined,
#      so it's always the one left standing.
# ============================================================


def majority_element_brute(nums):
    # Brute force: count each element with an inner loop.
    n = len(nums)
    for x in nums:
        count = 0
        for y in nums:
            if y == x:
                count += 1
        if count > n // 2:
            return x
    return -1


def majority_element_hashmap(nums):
    counts = {}
    half = len(nums) // 2
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > half:
            return num              # can return early the moment it crosses half
    return -1


def majority_element_boyer_moore(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num         # nobody's in charge, this number takes over
        if num == candidate:
            count += 1              # a supporter
        else:
            count -= 1              # an attacker cancels one supporter

    return candidate                # guaranteed to be the majority


if __name__ == "__main__":
    print(majority_element_hashmap([3, 2, 3]))                 # 3
    print(majority_element_boyer_moore([2, 2, 1, 1, 1, 2, 2])) # 2
    print(majority_element_brute([2, 2, 1, 1, 1, 2, 2]))       # 2
