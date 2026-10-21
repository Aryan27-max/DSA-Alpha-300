# ============================================================
# Day 8 - VARIANT: Palindromic Substrings  (LeetCode 647)
# ============================================================
# The question:
#   Count how many substrings of s are palindromes. Substrings at
#   different positions count separately, even if they look the same.
#
#   Example: "abc" -> 3  ("a", "b", "c")
#            "aaa" -> 6  ("a","a","a","aa","aa","aaa")
#
# The big idea (expand around the center):
#   Every palindrome has a center. It's either one character
#   (odd length, "aba") or the gap between two characters (even, "abba").
#   That's 2n - 1 centers. From each center, two pointers walk OUTWARD
#   while the ends match - every step outward is one more palindrome.
# ============================================================


def count_substrings_brute(s):
    # Brute force: check every substring with two pointers.
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            a, b = i, j
            ok = True
            while a < b:
                if s[a] != s[b]:
                    ok = False
                    break
                a += 1
                b -= 1
            if ok:
                count += 1
    return count


def expand(s, left, right):
    # Count palindromes found by growing outward from this center.
    found = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        found += 1
        left -= 1
        right += 1
    return found


def count_substrings(s):
    total = 0
    for i in range(len(s)):
        total += expand(s, i, i)        # odd length: center is s[i]
        total += expand(s, i, i + 1)    # even length: center is between s[i] and s[i+1]
    return total


if __name__ == "__main__":
    print(count_substrings("abc"))        # 3
    print(count_substrings("aaa"))        # 6
    print(count_substrings_brute("aaa"))  # 6
