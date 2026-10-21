# ============================================================
# Day 8 - VARIANT: Valid Palindrome II  (LeetCode 680)
# ============================================================
# The question:
#   Return True if the string can become a palindrome after deleting
#   AT MOST one character.
#
#   Example: "aba" -> True     "abca" -> True (delete 'c')     "abc" -> False
#
# The big idea (greedy skip):
#   Walk two pointers inward like normal. The first time they disagree,
#   we get exactly one deletion. Either delete the left char or the
#   right char - check if the remaining middle part is a palindrome
#   for EITHER choice.
# ============================================================


def is_pal_range(s, i, j):
    # Is s[i..j] a palindrome? (checked with two pointers, no slicing)
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def valid_palindrome_brute(s):
    # Brute force: try deleting every character one at a time.
    if is_pal_range(s, 0, len(s) - 1):
        return True
    for skip in range(len(s)):
        chars = []
        for k in range(len(s)):
            if k != skip:
                chars.append(s[k])
        if is_pal_range(chars, 0, len(chars) - 1):
            return True
    return False


def valid_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # first mismatch: use our one deletion, try both options
            return is_pal_range(s, left + 1, right) or is_pal_range(s, left, right - 1)
        left += 1
        right -= 1

    return True                     # never needed a deletion


if __name__ == "__main__":
    print(valid_palindrome("aba"))    # True
    print(valid_palindrome("abca"))   # True
    print(valid_palindrome("abc"))    # False
    print(valid_palindrome("deeee"))  # True
