# ============================================================
# Day 8 - VARIANT: Palindrome Number  (LeetCode 9)
# ============================================================
# The question:
#   Return True if the integer x reads the same forwards and backwards.
#   Follow-up: do it WITHOUT converting it to a string.
#
#   Example: 121 -> True     -121 -> False     10 -> False
#
# The big idea (reverse half of the number):
#   Negative numbers are never palindromes ("-121" vs "121-").
#   Numbers ending in 0 aren't either (except 0 itself).
#   Peel digits off the end with % 10 and build the reversed number,
#   but stop halfway - once reversed >= what's left of x.
#   Then compare. For odd digit counts, drop the middle digit with // 10.
# ============================================================


def is_palindrome_brute(x):
    # String version (the thing the follow-up asks us to avoid).
    s = str(x)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10   # take the last digit of x
        x //= 10                                      # remove it from x

    # even digits: x == reversed_half; odd digits: middle digit sits at the end of reversed_half
    return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    print(is_palindrome(121))      # True
    print(is_palindrome(-121))     # False
    print(is_palindrome(10))       # False
    print(is_palindrome(12321))    # True
    print(is_palindrome(0))        # True
