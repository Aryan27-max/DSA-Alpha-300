# ============================================================
# Day 7 - VARIANT: Intersection of Two Arrays  (LeetCode 349)
# ============================================================
# The question:
#   Return the numbers that appear in BOTH lists. Each number in the
#   answer must be unique (no duplicates).
#
#   Example: nums1 = [1, 2, 2, 1], nums2 = [2, 2] -> [2]
#
# The big idea:
#   Here we only care about yes/no, not how many -> a set is enough.
#   Put nums1 in a set. Walk nums2; when a number is in the set,
#   add it to the answer and REMOVE it from the set so it can't be added twice.
#   (No & operator - we build the logic ourselves.)
# ============================================================


def intersection_brute(nums1, nums2):
    # Brute force: compare everything, avoid repeats by checking the result list.
    result = []
    for a in nums1:
        for b in nums2:
            if a == b:
                already = False
                for r in result:
                    if r == a:
                        already = True
                        break
                if not already:
                    result.append(a)
                break
    return result


def intersection(nums1, nums2):
    first = set()
    for num in nums1:
        first.add(num)

    result = []
    for num in nums2:
        if num in first:
            result.append(num)
            first.discard(num)      # remove it so we don't add the same number again

    return result


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))           # [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))     # [9, 4] (any order)
