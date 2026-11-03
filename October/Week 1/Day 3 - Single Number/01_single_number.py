# ============================================================
# Day 3 - PRIMARY: Single Number  (LeetCode 136)
# ============================================================
# The question:
#   Every number appears exactly twice, except one number that appears once.
#   Find that lonely number. Use O(n) time and O(1) extra space.
#
#   Example: [4, 1, 2, 1, 2] -> 4
#
# The big idea (XOR):
#   XOR (^) has three magic rules:
#     a ^ a = 0        (a number cancels itself)
#     a ^ 0 = a        (XOR with zero changes nothing)
#     order doesn't matter
#   So if we XOR everything together, every pair cancels to 0,
#   and only the single number is left standing.
# ============================================================


def single_number_brute(nums):
    # Brute force: for each number, count how often it appears.
    for x in nums:
        count = 0
        for y in nums:
            if x == y:
                count += 1
        if count == 1:
            return x
    return None


def single_number(nums):
    result = 0
    for num in nums:
        result ^= num       # pairs cancel each other out
    return result           # whatever survives is the single one


if __name__ == "__main__":
    print(single_number([2, 2, 1]))         # 1
    print(single_number([4, 1, 2, 1, 2]))   # 4
    print(single_number([1]))               # 1
