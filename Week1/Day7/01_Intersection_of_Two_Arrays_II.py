# Intersection of Two Arrays II
#
# We need duplicates in the answer, so just checking whether a value
# exists is not enough. We need to remember how many times it appears.
#
# Example:
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# answer = [2, 2]


def intersect(nums1, nums2):
    freq = {}

    # Count how many times every number appears in nums1.
    for x in nums1:
        if x not in freq:
            freq[x] = 0
        freq[x] += 1

    answer = []

    # Use one occurrence whenever we find the same number in nums2.
    for x in nums2:
        if x in freq and freq[x] > 0:
            answer.append(x)
            freq[x] -= 1

    return answer


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print("Intersection:", intersect(nums1, nums2))
