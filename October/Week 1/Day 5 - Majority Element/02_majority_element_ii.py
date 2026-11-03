# ============================================================
# Day 5 - VARIANT: Majority Element II  (LeetCode 229)
# ============================================================
# The question:
#   Return ALL elements that appear more than n / 3 times.
#   There can be at most 2 such elements (3 of them would be > n total).
#
#   Example: [3, 2, 3] -> [3]       [1, 2] -> [1, 2]
#
# The big idea (Boyer-Moore with two candidates):
#   Keep two candidates and two counts.
#   - Number matches a candidate -> that count goes up.
#   - A count is 0 -> this number becomes that candidate.
#   - Matches neither -> BOTH counts go down (it cancels one of each).
#   At the end the candidates are only "possible" answers, so do a
#   second pass to actually count them and confirm.
# ============================================================


def majority_element_ii_brute(nums):
    # Hashmap version: O(n) time, O(n) space.
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    limit = len(nums) // 3
    result = []
    for num in counts:
        if counts[num] > limit:
            result.append(num)
    return result


def majority_element_ii(nums):
    cand1, cand2 = None, None
    count1, count2 = 0, 0

    # Pass 1: find up to two candidates
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1             # num cancels one vote from each candidate
            count2 -= 1

    # Pass 2: verify - candidates are not guaranteed to be real answers
    count1, count2 = 0, 0
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1

    result = []
    limit = len(nums) // 3
    if count1 > limit:
        result.append(cand1)
    if count2 > limit:
        result.append(cand2)
    return result


if __name__ == "__main__":
    print(majority_element_ii([3, 2, 3]))                  # [3]
    print(majority_element_ii([1]))                        # [1]
    print(majority_element_ii([1, 2]))                     # [1, 2]
    print(majority_element_ii([2, 2, 1, 1, 1, 2, 2, 3]))   # [2, 1]  (2 appears 4 times, 1 appears 3 times, both > 8/3)
