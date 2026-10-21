# ============================================================
# Day 9 - VARIANT: Reverse String II  (LeetCode 541)
# ============================================================
# The question:
#   For every block of 2k characters, reverse the FIRST k of them and
#   leave the next k alone.
#   - If fewer than k are left, reverse all of them.
#   - If between k and 2k are left, reverse the first k only.
#
#   Example: s = "abcdefg", k = 2 -> "bacdfeg"
#
# The big idea:
#   Jump through the string in steps of 2k. At each start, run the
#   normal two-pointer swap on [start, start + k - 1], making sure the
#   right end doesn't go past the end of the string.
# ============================================================


def reverse_range(chars, left, right):
    # The Day 9 swap loop, on just a piece of the list.
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


def reverse_str_brute(s, k):
    # "Brute" version: build each chunk by reading it backwards into a new list.
    result = []
    n = len(s)
    for start in range(0, n, 2 * k):
        end = start + k
        if end > n:
            end = n
        for i in range(end - 1, start - 1, -1):    # first k, backwards
            result.append(s[i])
        for i in range(end, min(start + 2 * k, n)):  # next k, as-is
            result.append(s[i])
    return "".join(result)


def reverse_str(s, k):
    chars = list(s)
    n = len(chars)

    for start in range(0, n, 2 * k):
        right = start + k - 1
        if right > n - 1:
            right = n - 1               # fewer than k left -> reverse whatever's there
        reverse_range(chars, start, right)

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_str("abcdefg", 2))   # bacdfeg
    print(reverse_str("abcd", 2))      # bacd
    print(reverse_str("abc", 5))       # cba
