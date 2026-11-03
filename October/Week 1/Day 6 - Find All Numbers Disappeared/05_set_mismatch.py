# ============================================================
# Day 6 - VARIANT: Set Mismatch  (LeetCode 645)
# ============================================================
# The question:
#   The list should contain 1..n exactly once, but by mistake one
#   number got duplicated, replacing another number.
#   Return [the duplicated number, the missing number].
#
#   Example: [1, 2, 2, 4] -> [2, 3]
#
# The big idea (negative marking - both answers in one go):
#   Pass 1: for value v, flip nums[v-1] negative.
#           If it's already negative, v is the duplicate.
#   Pass 2: the index still positive is the missing number's home.
# ============================================================


def find_error_nums_brute(nums):
    # Dict counting: O(n) space.
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    dup = missing = -1
    for v in range(1, len(nums) + 1):
        c = counts.get(v, 0)
        if c == 2:
            dup = v
        elif c == 0:
            missing = v
    return [dup, missing]


def find_error_nums(nums):
    dup = -1

    for i in range(len(nums)):
        v = abs(nums[i])
        home = v - 1
        if nums[home] < 0:
            dup = v                     # someone already marked this home -> duplicate
        else:
            nums[home] = -nums[home]

    missing = -1
    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1             # never marked -> missing
            break

    return [dup, missing]


if __name__ == "__main__":
    print(find_error_nums([1, 2, 2, 4]))   # [2, 3]
    print(find_error_nums([1, 1]))         # [1, 2]
    print(find_error_nums([3, 2, 2]))      # [2, 1]
