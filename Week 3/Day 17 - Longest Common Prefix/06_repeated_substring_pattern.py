# ============================================================
# Day 17 - VARIANT: Repeated Substring Pattern  (LeetCode 459)
# ============================================================
# The question:
#   Can s be built by repeating one of its substrings two or more times?
#
#   Example: "abab" -> True ("ab" x2)     "aba" -> False
#            "abcabcabcabc" -> True ("abc" x4)
#
# The big idea (KMP's LPS table):
#   Build the LPS table for s (same helper as Rotate String).
#   lps[n-1] = length of the longest prefix that is also a suffix.
#   If s is made of a repeating block, that block has length n - lps[n-1],
#   and it must divide n evenly.
#     "abcabcabc": lps[-1] = 6, block = 9 - 6 = 3, 9 % 3 == 0 -> True
# ============================================================


def repeated_substring_pattern_brute(s):
    # Brute force: try every block length that divides n.
    n = len(s)
    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue
        ok = True
        for i in range(size, n):
            if s[i] != s[i - size]:     # every char must equal the one a block earlier
                ok = False
                break
        if ok:
            return True
    return False


def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            i += 1
    return lps


def repeated_substring_pattern(s):
    n = len(s)
    lps = build_lps(s)
    longest = lps[n - 1]
    block = n - longest
    return longest > 0 and n % block == 0


if __name__ == "__main__":
    print(repeated_substring_pattern("abab"))           # True
    print(repeated_substring_pattern("aba"))            # False
    print(repeated_substring_pattern("abcabcabcabc"))   # True
    print(repeated_substring_pattern("abac"))           # False
