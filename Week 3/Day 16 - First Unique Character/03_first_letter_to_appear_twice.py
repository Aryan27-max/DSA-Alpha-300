# ============================================================
# Day 16 - VARIANT: First Letter to Appear Twice  (LeetCode 2351)
# ============================================================
# The question:
#   Return the first letter whose SECOND occurrence comes earliest.
#   (There's guaranteed to be at least one repeated letter.)
#
#   Example: "abccbaacz" -> "c"   (c's second copy is at index 3, the earliest)
#
# The big idea (first repeat in a stream):
#   Unlike the primary, we don't need two passes. Read left to right like
#   a stream, keeping a set of letters seen so far. The first letter that's
#   already in the set is the answer - stop right there.
# ============================================================


def repeated_character_brute(s):
    # Brute force: for each position j, look back to see if s[j] appeared before.
    for j in range(len(s)):
        for i in range(j):
            if s[i] == s[j]:
                return s[j]
    return ""


def repeated_character(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch               # second time we've met it - and it's the earliest
        seen.add(ch)
    return ""


if __name__ == "__main__":
    print(repeated_character("abccbaacz"))   # c
    print(repeated_character("abcdd"))       # d
