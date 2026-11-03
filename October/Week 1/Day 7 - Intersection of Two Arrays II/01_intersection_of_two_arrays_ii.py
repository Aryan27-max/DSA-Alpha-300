# ============================================================
# Day 7 - PRIMARY: Intersection of Two Arrays II  (LeetCode 350)
# ============================================================
# The question:
#   Return the intersection of two lists, KEEPING duplicates.
#   Each element should appear as many times as it shows up in BOTH.
#
#   Example: nums1 = [1, 2, 2, 1], nums2 = [2, 2] -> [2, 2]
#            nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4] -> [4, 9]
#
# The big idea (multiset = a dict of counts):
#   A set only remembers "yes/no". Here we need "how many", so we use
#   a count dict. Count nums1, then walk nums2: if the count is > 0,
#   add it to the answer and use up one copy (decrement).
#   Tip: count the SMALLER list to save memory.
# ============================================================


def intersect_brute(nums1, nums2):
    # Brute force: for each number in nums1, find an unused match in nums2.
    used = [False] * len(nums2)
    result = []
    for a in nums1:
        for j in range(len(nums2)):
            if not used[j] and nums2[j] == a:
                used[j] = True          # this copy is taken now
                result.append(a)
                break
    return result


def intersect(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1     # build the dict on the smaller list

    counts = {}
    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    result = []
    for num in nums2:
        if counts.get(num, 0) > 0:
            result.append(num)
            counts[num] -= 1            # one copy used up

    return result


if __name__ == "__main__":
    print(intersect([1, 2, 2, 1], [2, 2]))            # [2, 2]
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))      # [4, 9] (any order)
