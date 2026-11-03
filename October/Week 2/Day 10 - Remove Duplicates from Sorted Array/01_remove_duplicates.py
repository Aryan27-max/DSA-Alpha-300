# ============================================================
# Day 10 - PRIMARY: Remove Duplicates from Sorted Array  (LeetCode 26)
# ============================================================
# The question:
#   The list is sorted. Remove duplicates IN PLACE so every value appears
#   once. Return k = number of unique values. The first k slots must hold
#   them in order; what's after slot k doesn't matter.
#
#   Example: [0,0,1,1,1,2,2,3,3,4] -> k = 5, first five = [0,1,2,3,4]
#
# The big idea (read pointer + write pointer):
#   - read walks over every element.
#   - write marks where the next unique value should go.
#   Because the list is sorted, a value is "new" if it differs from the
#   last value we wrote. When it is, copy it to nums[write] and move write.
#   (No list(set(nums)) - that loses order and isn't in place.)
# ============================================================


def remove_duplicates_brute(nums):
    # Brute force: whenever two neighbours match, delete one with pop(i)
    # (pop from the middle shifts everything left - O(n) each time).
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    write = 1                               # nums[0] is always kept
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:   # different from the last kept value?
            nums[write] = nums[read]        # keep it
            write += 1

    return write                            # number of unique values


if __name__ == "__main__":
    a = [1, 1, 2]
    k = remove_duplicates(a)
    print(k, a[:k])     # 2 [1, 2]

    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(b)
    print(k, b[:k])     # 5 [0, 1, 2, 3, 4]
