# ============================================================
# Day 7 - VARIANT: Find the Difference of Two Arrays  (LeetCode 2215)
# ============================================================
# The question:
#   Return a list of two lists:
#     answer[0] = distinct numbers in nums1 that are NOT in nums2
#     answer[1] = distinct numbers in nums2 that are NOT in nums1
#
#   Example: nums1 = [1, 2, 3], nums2 = [2, 4, 6] -> [[1, 3], [4, 6]]
#
# The big idea:
#   Build a set for each list (by hand). Then walk each set and keep
#   the numbers the OTHER set doesn't have. Using sets also removes
#   duplicates for free. (No set subtraction operator - do it by hand.)
# ============================================================


def find_difference_brute(nums1, nums2):
    # Brute force: for every number, scan the other list. Avoid repeats manually.
    def only_in(a, b):
        out = []
        for x in a:
            in_b = False
            for y in b:
                if x == y:
                    in_b = True
                    break
            if not in_b:
                dup = False
                for o in out:
                    if o == x:
                        dup = True
                        break
                if not dup:
                    out.append(x)
        return out

    return [only_in(nums1, nums2), only_in(nums2, nums1)]


def find_difference(nums1, nums2):
    set1 = set()
    for x in nums1:
        set1.add(x)
    set2 = set()
    for x in nums2:
        set2.add(x)

    only1 = []
    for x in set1:
        if x not in set2:
            only1.append(x)         # in nums1 but missing from nums2

    only2 = []
    for x in set2:
        if x not in set1:
            only2.append(x)         # in nums2 but missing from nums1

    return [only1, only2]


if __name__ == "__main__":
    print(find_difference([1, 2, 3], [2, 4, 6]))         # [[1, 3], [4, 6]]
    print(find_difference([1, 2, 3, 3], [1, 1, 2, 2]))   # [[3], []]
