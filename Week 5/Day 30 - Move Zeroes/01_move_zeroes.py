# ============================================================
# Day 30 - PRIMARY: Move Zeroes  (LeetCode 283)
# ============================================================
# The question:
#   Move every 0 to the end of the list IN PLACE, keeping the non-zero
#   numbers in their original order. O(1) extra space.
#
#   Example: [0,1,0,3,12] -> [1,3,12,0,0]
#
# The big idea (read + write pointers - same muscle as Remove Duplicates):
#   read  walks over every element.
#   write is where the next non-zero belongs.
#   When read finds a non-zero, SWAP it with nums[write] and move write.
#   Everything before write is "non-zeros, in order"; between write and
#   read are only zeros. Swapping (instead of copying) means the zeros
#   are pushed back automatically.
#
#   Alternative (fewer writes): copy non-zeros forward first, then fill
#   the rest with zeros. Both O(n), O(1) space.
#   (No sort(key=...), no filter(), no [x for x in nums if x != 0] + padding.)
# ============================================================


def move_zeroes_brute(nums):
    # Brute force: bubble each zero rightward one swap at a time. O(n^2).
    n = len(nums)
    for _ in range(n):
        for i in range(n - 1):
            if nums[i] == 0 and nums[i + 1] != 0:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


def move_zeroes_copy_then_fill(nums):
    write = 0
    for x in nums:
        if x != 0:
            nums[write] = x             # copy non-zeros forward
            write += 1
    while write < len(nums):
        nums[write] = 0                 # everything after is zero
        write += 1


def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    print(a)        # [1, 3, 12, 0, 0]

    b = [0]
    move_zeroes(b)
    print(b)        # [0]

    c = [4, 0, 0, 5, 0, 6]
    move_zeroes_copy_then_fill(c)
    print(c)        # [4, 5, 6, 0, 0, 0]
