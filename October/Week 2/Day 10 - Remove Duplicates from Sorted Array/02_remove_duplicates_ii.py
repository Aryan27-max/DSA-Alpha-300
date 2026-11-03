# ============================================================
# Day 10 - VARIANT: Remove Duplicates from Sorted Array II  (LeetCode 80)
# ============================================================
# The question:
#   Sorted list. Remove extra copies in place so each value appears
#   AT MOST TWICE. Return k, the new length.
#
#   Example: [1,1,1,2,2,3] -> k = 5, first five = [1,1,2,2,3]
#
# The big idea:
#   Same read/write pointers. Rule to keep nums[read]:
#   it must be different from nums[write - 2] (the value two slots back
#   in the kept part). If it equals that, we already have two copies.
#   Change the 2 to any number to allow "at most k copies".
# ============================================================


def remove_duplicates_brute(nums):
    # Count run lengths and pop extras (slow because pop shifts elements).
    i = 0
    while i < len(nums):
        j = i
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        run = j - i
        while run > 2:
            nums.pop(i)
            run -= 1
        i += run
    return len(nums)


def remove_duplicates(nums):
    write = 0
    for read in range(len(nums)):
        # always keep the first two; after that only keep if it's not a 3rd copy
        if write < 2 or nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    return write


if __name__ == "__main__":
    a = [1, 1, 1, 2, 2, 3]
    k = remove_duplicates(a)
    print(k, a[:k])     # 5 [1, 1, 2, 2, 3]

    b = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = remove_duplicates(b)
    print(k, b[:k])     # 7 [0, 0, 1, 1, 2, 3, 3]
