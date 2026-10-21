# ============================================================
# Day 10 - VARIANT: Sort Colors  (LeetCode 75)
# ============================================================
# The question:
#   The list only has 0s, 1s and 2s (red, white, blue). Sort it IN PLACE
#   in one pass without using a sort function.
#
#   Example: [2,0,2,1,1,0] -> [0,0,1,1,2,2]
#
# The big idea (Dutch National Flag - three pointers):
#   low  = where the next 0 should go
#   mid  = the element we're looking at
#   high = where the next 2 should go
#   - nums[mid] == 0 -> swap with low, move low and mid forward
#   - nums[mid] == 1 -> it's already in the middle, just move mid
#   - nums[mid] == 2 -> swap with high, move high back
#     (DON'T move mid - the number we just swapped in hasn't been checked)
# ============================================================


def sort_colors_brute(nums):
    # Counting sort: count 0s, 1s, 2s, then rewrite. Two passes.
    c0 = c1 = c2 = 0
    for x in nums:
        if x == 0:
            c0 += 1
        elif x == 1:
            c1 += 1
        else:
            c2 += 1
    i = 0
    for _ in range(c0):
        nums[i] = 0; i += 1
    for _ in range(c1):
        nums[i] = 1; i += 1
    for _ in range(c2):
        nums[i] = 2; i += 1


def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1           # mid stays: the swapped-in value still needs checking


if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    sort_colors(a)
    print(a)    # [0, 0, 1, 1, 2, 2]

    b = [2, 0, 1]
    sort_colors(b)
    print(b)    # [0, 1, 2]
