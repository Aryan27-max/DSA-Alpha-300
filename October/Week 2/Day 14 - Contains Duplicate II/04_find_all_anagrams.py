# ============================================================
# Day 14 - VARIANT: Find All Anagrams in a String  (LeetCode 438)
# ============================================================
# The question:
#   Return every start index in s where a substring is an anagram of p.
#
#   Example: s = "cbaebabacd", p = "abc" -> [0, 6]
#
# Day 13 vs Day 14:
#   Day 13 used two 26-slot arrays and a 'matches' counter.
#   Today, reuse the Permutation in String code with a hashmap - it works
#   for ANY characters (not just a-z). The only change: instead of
#   returning True the first time, collect every start index.
# ============================================================


def find_anagrams_brute(s, p):
    # Brute force: rebuild the count dict for every window.
    def count(text, start, length):
        c = {}
        for i in range(start, start + length):
            c[text[i]] = c.get(text[i], 0) + 1
        return c

    k = len(p)
    target = count(p, 0, k)
    result = []
    for i in range(len(s) - k + 1):
        if count(s, i, k) == target:
            result.append(i)
    return result


def find_anagrams(s, p):
    k = len(p)
    result = []
    if k > len(s):
        return result

    need = {}
    for ch in p:
        need[ch] = need.get(ch, 0) + 1
    missing = k

    for right in range(len(s)):
        ch = s[right]
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1

        if right >= k:
            out = s[right - k]
            need[out] += 1
            if need[out] > 0:
                missing += 1

        if missing == 0:
            result.append(right - k + 1)    # start of the current window

    return result


if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))         # [0, 6]
    print(find_anagrams("abab", "ab"))                # [0, 1, 2]
    print(find_anagrams_brute("cbaebabacd", "abc"))   # [0, 6]
