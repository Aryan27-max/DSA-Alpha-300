# ============================================================
# Day 26 - VARIANT: Next Greater Element III  (LeetCode 556)
# ============================================================
# The question:
#   Given a positive integer n, return the SMALLEST integer that uses
#   exactly the same digits and is bigger than n. If none exists, or the
#   answer doesn't fit in a 32-bit signed int, return -1.
#
#   Example: 12 -> 21      21 -> -1      534976 -> 536479
#
# The big idea (next permutation - a stack-shaped scan):
#   Look at the digits from the RIGHT. While they keep going up
#   (reading leftward), that tail is already as big as it can be - just
#   like values piling up in a monotonic stack.
#   1. Find the first digit (from the right) that is SMALLER than the
#      digit after it. Call its index i. (No such i -> -1.)
#   2. In the tail to its right, find the smallest digit that is still
#      bigger than digits[i], and swap them.
#   3. The tail is still in descending order - reverse it (Day 9 swap)
#      to make it as small as possible.
#   534976: i points at 4 (since 4 < 9). Swap with 6 -> 536974.
#           Reverse the tail "974" -> "479" -> 536479.
# ============================================================

LIMIT = 2 ** 31 - 1


def next_greater_element_brute(n):
    # Brute force: try every arrangement of the digits, keep the smallest > n.
    digits = list(str(n))
    used = [False] * len(digits)
    best = [-1]

    def build(current):
        if len(current) == len(digits):
            value = int("".join(current))
            if value > n and value <= LIMIT and (best[0] == -1 or value < best[0]):
                best[0] = value
            return
        for i in range(len(digits)):
            if not used[i]:
                used[i] = True
                current.append(digits[i])
                build(current)
                current.pop()
                used[i] = False

    build([])
    return best[0]


def next_greater_element(n):
    digits = list(str(n))
    size = len(digits)

    # 1. find the pivot
    i = size - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i < 0:
        return -1                       # digits are in descending order - already the max

    # 2. swap the pivot with the smallest bigger digit on its right
    j = size - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]

    # 3. reverse the tail to make it as small as possible
    left, right = i + 1, size - 1
    while left < right:
        digits[left], digits[right] = digits[right], digits[left]
        left += 1
        right -= 1

    value = int("".join(digits))
    return value if value <= LIMIT else -1


if __name__ == "__main__":
    print(next_greater_element(12))            # 21
    print(next_greater_element(21))            # -1
    print(next_greater_element(534976))        # 536479
    print(next_greater_element(2147483486))    # -1 (answer would overflow)
