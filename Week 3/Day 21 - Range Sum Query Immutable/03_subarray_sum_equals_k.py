# ============================================================
# Day 21 - VARIANT: Subarray Sum Equals K  (LeetCode 560)
# ============================================================
# The question:
#   Count the contiguous subarrays whose sum is exactly k.
#   Numbers can be negative, so sliding windows DON'T work here.
#
#   Example: nums = [1,1,1], k = 2 -> 2
#            nums = [1,2,3], k = 3 -> 2   ([1,2] and [3])
#
# The big idea (prefix sum + hashmap - Two Sum on prefixes!):
#   sum(nums[i..j]) = prefix[j] - prefix[i-1].
#   We want that to equal k  ->  prefix[i-1] = prefix[j] - k.
#   So as we walk, ask: "how many earlier prefixes equal (current - k)?"
#   Keep a dict: prefix value -> how many times we've seen it.
#   Start with {0: 1} - the empty prefix, so subarrays starting at index 0
#   are counted too.
#   That's exactly Day 1's Two Sum pattern, applied to prefix sums.
# ============================================================


def subarray_sum_brute(nums, k):
    # Brute force: every start, extend and count matches.
    count = 0
    n = len(nums)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s == k:
                count += 1
    return count


def subarray_sum(nums, k):
    seen = {0: 1}                       # prefix sum 0 has "happened" once (before we start)
    prefix = 0
    count = 0

    for x in nums:
        prefix += x
        need = prefix - k               # an earlier prefix with this value gives a sum of k
        count += seen.get(need, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))           # 2
    print(subarray_sum([1, 2, 3], 3))           # 2
    print(subarray_sum([1, -1, 0], 0))          # 3
    print(subarray_sum_brute([1, -1, 0], 0))    # 3
