# Intersection of Two Arrays
#
# This version only wants unique values.
# We manually keep track of values we have already added instead of
# using set intersection directly.


def intersection(nums1, nums2):
    present = {}
    added = {}

    # Mark values that exist in the first array.
    for x in nums1:
        present[x] = True

    answer = []

    # Add a value only if it exists in nums1 and has not been added yet.
    for x in nums2:
        if x in present and x not in added:
            answer.append(x)
            added[x] = True

    return answer


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print("Unique intersection:", intersection(nums1, nums2))
