# ============================================================
# Day 10 - VARIANT: Move Zeroes  (LeetCode 283)
# ============================================================
# The question:
#   Move all 0s to the end IN PLACE, keeping the order of the non-zero
#   numbers the same.
#
#   Example: [0,1,0,3,12] -> [1,3,12,0,0]
#
# The big idea:
#   read/write pointers, but SWAP instead of copy.
#   Every time read finds a non-zero, swap it into nums[write].
#   Zeros naturally drift to the back, and nothing gets overwritten.
# ============================================================


def move_zeroes_brute(nums):
    # Copy non-zeros into a new list, pad with zeros, copy back. O(n) space.
    temp = []
    for x in nums:
        if x != 0:
            temp.append(x)
    while len(temp) < len(nums):
        temp.append(0)
    for i in range(len(nums)):
        nums[i] = temp[i]


def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]   # non-zero moves forward
            write += 1


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    print(a)    # [1, 3, 12, 0, 0]

    b = [0]
    move_zeroes(b)
    print(b)    # [0]
