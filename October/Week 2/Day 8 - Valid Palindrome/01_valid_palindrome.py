# ============================================================
# Day 8 - PRIMARY: Valid Palindrome  (LeetCode 125)
# ============================================================
# The question:
#   A phrase is a palindrome if, after lowercasing everything and
#   throwing away anything that's not a letter or digit, it reads the
#   same forwards and backwards. Return True or False.
#
#   Example: "A man, a plan, a canal: Panama" -> True
#            "race a car"                     -> False
#
# The big idea (two pointers from the ends):
#   Put one pointer at the start and one at the end.
#   - If a pointer is sitting on junk (space, comma...), step past it.
#   - Otherwise compare the two characters (lowercased).
#   - Mismatch? Not a palindrome. Match? Move both inward.
#   We clean up ON THE WAY instead of building a new cleaned string,
#   so we use O(1) extra space. (No s == s[::-1]!)
# ============================================================


def is_palindrome_brute(s):
    # Brute force: build a cleaned list first, then compare from both ends.
    cleaned = []
    for ch in s:
        if ch.isalnum():
            cleaned.append(ch.lower())
    i, j = 0, len(cleaned) - 1
    while i < j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # skip junk on the left
        if not s[left].isalnum():
            left += 1
            continue
        # skip junk on the right
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False            # the two ends don't match

        left += 1                   # matched, move both inward
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))   # True
    print(is_palindrome("race a car"))                       # False
    print(is_palindrome(" "))                                # True
    print(is_palindrome_brute("0P"))                         # False
