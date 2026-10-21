# ============================================================
# Day 13 - VARIANT: Find All Anagrams in a String  (LeetCode 438)
# ============================================================
# The question:
#   Return every start index in s where a substring is an anagram of p
#   (same letters, same counts, any order).
#
#   Example: s = "cbaebabacd", p = "abc" -> [0, 6]
#
# The big idea (fixed window + frequency match):
#   The window is always len(p) long.
#   Keep 26-slot letter counts for p and for the current window.
#   Instead of comparing all 26 slots every step, track 'matches' =
#   how many of the 26 letters currently have equal counts.
#   When matches == 26, the window is an anagram.
# ============================================================


def find_anagrams_brute(s, p):
    # Brute force: count letters of every window from scratch and compare.
    def counts(text, start, length):
        c = [0] * 26
        for i in range(start, start + length):
            c[ord(text[i]) - 97] += 1
        return c

    target = counts(p, 0, len(p))
    result = []
    for i in range(len(s) - len(p) + 1):
        if counts(s, i, len(p)) == target:
            result.append(i)
    return result


def find_anagrams(s, p):
    k = len(p)
    if k > len(s):
        return []

    need = [0] * 26
    have = [0] * 26
    for i in range(k):
        need[ord(p[i]) - 97] += 1
        have[ord(s[i]) - 97] += 1

    matches = 0
    for i in range(26):
        if need[i] == have[i]:
            matches += 1

    result = []
    if matches == 26:
        result.append(0)

    for right in range(k, len(s)):
        # letter coming in
        c = ord(s[right]) - 97
        if have[c] == need[c]:
            matches -= 1                # was matching, about to break
        have[c] += 1
        if have[c] == need[c]:
            matches += 1                # now matches

        # letter going out
        c = ord(s[right - k]) - 97
        if have[c] == need[c]:
            matches -= 1
        have[c] -= 1
        if have[c] == need[c]:
            matches += 1

        if matches == 26:
            result.append(right - k + 1)    # window start

    return result


if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))      # [0, 6]
    print(find_anagrams("abab", "ab"))             # [0, 1, 2]
    print(find_anagrams_brute("cbaebabacd", "abc"))  # [0, 6]
