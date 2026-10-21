# ============================================================
# Day 11 - PRIMARY: Merge Sorted Array  (LeetCode 88)
# ============================================================
# The question:
#   nums1 has m real numbers followed by n empty slots (zeros).
#   nums2 has n numbers. Both are sorted. Merge nums2 INTO nums1 so that
#   nums1 becomes one sorted list of length m + n. Return nothing.
#
#   Example: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#            -> nums1 = [1,2,2,3,5,6]
#
# The big idea (three pointers from the END):
#   If we fill from the front, we'd overwrite nums1's numbers before using
#   them. But the BACK of nums1 is empty space! So:
#     i = last real number in nums1
#     j = last number in nums2
#     w = last slot of nums1 (where the biggest number goes)
#   Each step, put the bigger of nums1[i] / nums2[j] at w, move back.
#   When nums2 runs out we're done - nums1's leftovers are already in place.
#   (No sorted(nums1 + nums2) or heapq.merge().)
# ============================================================


def merge_brute(nums1, m, nums2, n):
    # Brute force: merge from the front into a new list, then copy back. O(m+n) space.
    merged = []
    i = j = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i]); i += 1
        else:
            merged.append(nums2[j]); j += 1
    while i < m:
        merged.append(nums1[i]); i += 1
    while j < n:
        merged.append(nums2[j]); j += 1
    for k in range(m + n):
        nums1[k] = merged[k]


def merge(nums1, m, nums2, n):
    i = m - 1           # last real value in nums1
    j = n - 1           # last value in nums2
    w = m + n - 1       # write position at the very end

    while j >= 0:                           # stop once nums2 is fully placed
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[w] = nums1[i]             # nums1's value is bigger, it goes last
            i -= 1
        else:
            nums1[w] = nums2[j]             # nums2's value is bigger (or nums1 is used up)
            j -= 1
        w -= 1


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    merge(a, 3, [2, 5, 6], 3)
    print(a)    # [1, 2, 2, 3, 5, 6]

    b = [0]
    merge(b, 0, [1], 1)
    print(b)    # [1]

    c = [4, 5, 6, 0, 0, 0]
    merge_brute(c, 3, [1, 2, 3], 3)
    print(c)    # [1, 2, 3, 4, 5, 6]
