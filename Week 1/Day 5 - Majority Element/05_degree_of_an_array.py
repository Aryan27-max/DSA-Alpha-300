# ============================================================
# Day 5 - VARIANT: Degree of an Array  (LeetCode 697)
# ============================================================
# The question:
#   The "degree" of an array = the highest frequency of any element.
#   Find the length of the SHORTEST contiguous subarray that has the
#   same degree as the whole array.
#
#   Example: [1, 2, 2, 3, 1] -> 2
#     degree is 2 (both 1 and 2 appear twice).
#     shortest piece with degree 2 is [2, 2], length 2.
#
# The big idea:
#   For each number track: how many times, first index, last index.
#   For numbers with the max count, the shortest piece that holds all
#   of their copies is (last - first + 1). Take the smallest of those.
# ============================================================


def find_shortest_subarray_brute(nums):
    # Brute force: check every subarray, compute its degree.
    full_degree = 0
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > full_degree:
            full_degree = counts[num]

    n = len(nums)
    for length in range(1, n + 1):          # try smallest lengths first
        for start in range(n - length + 1):
            c = {}
            deg = 0
            for k in range(start, start + length):
                c[nums[k]] = c.get(nums[k], 0) + 1
                if c[nums[k]] > deg:
                    deg = c[nums[k]]
            if deg == full_degree:
                return length
    return n


def find_shortest_subarray(nums):
    count = {}
    first = {}
    last = {}

    for i in range(len(nums)):
        num = nums[i]
        if num not in first:
            first[num] = i          # first time we see it
        last[num] = i               # keep updating, ends at the last time
        count[num] = count.get(num, 0) + 1

    degree = 0
    for num in count:
        if count[num] > degree:
            degree = count[num]

    best = len(nums)
    for num in count:
        if count[num] == degree:
            length = last[num] - first[num] + 1
            if length < best:
                best = length

    return best


if __name__ == "__main__":
    print(find_shortest_subarray([1, 2, 2, 3, 1]))          # 2
    print(find_shortest_subarray([1, 2, 2, 3, 1, 4, 2]))    # 6
    print(find_shortest_subarray_brute([1, 2, 2, 3, 1]))    # 2
