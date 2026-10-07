# Union of Two Arrays
#
# Here duplicates should stay.
# So we count all occurrences from both arrays and then rebuild
# the result from those counts.


def union_with_duplicates(nums1, nums2):
    freq = {}

    # Count values from the first array.
    for x in nums1:
        if x not in freq:
            freq[x] = 0
        freq[x] += 1

    # Add the counts from the second array.
    for x in nums2:
        if x not in freq:
            freq[x] = 0
        freq[x] += 1

    answer = []

    # Put each value into the result as many times as it occurred.
    for value in freq:
        count = freq[value]

        while count > 0:
            answer.append(value)
            count -= 1

    return answer


nums1 = [1, 2, 2]
nums2 = [2, 3]

print("Union with duplicates:", union_with_duplicates(nums1, nums2))
