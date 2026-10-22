# ============================================================
# Day 15 - VARIANT: Find All Anagrams in a String  (LeetCode 438)
# ============================================================
# The question:
#   Return every start index in s where the substring is an anagram of p.
#
#   Example: s = "cbaebabacd", p = "abc" -> [0, 6]
#
# The big idea (window + anagram):
#   Third time you've met this one (Day 13 and Day 14 too). Today's angle
#   is pure frequency counting: one 'balance' dict like the primary.
#     - p's letters start at +1 each ("I still need these").
#     - A letter entering the window does -1, a letter leaving does +1.
#     - Track 'nonzero' = how many letters have balance != 0.
#   nonzero == 0 means the window's counts match p exactly.
# ============================================================


def find_anagrams_brute(s, p):
    # Brute force: run the primary's anagram check on every window.
    k = len(p)
    result = []
    for i in range(len(s) - k + 1):
        balance = {}
        for j in range(k):
            balance[p[j]] = balance.get(p[j], 0) + 1
            balance[s[i + j]] = balance.get(s[i + j], 0) - 1
        ok = True
        for ch in balance:
            if balance[ch] != 0:
                ok = False
                break
        if ok:
            result.append(i)
    return result


def adjust(balance, ch, delta, nonzero):
    # Change one letter's balance and keep the 'nonzero' tally correct.
    before = balance.get(ch, 0)
    after = before + delta
    balance[ch] = after
    if before == 0 and after != 0:
        nonzero += 1
    elif before != 0 and after == 0:
        nonzero -= 1
    return nonzero


def find_anagrams(s, p):
    k = len(p)
    result = []
    if k > len(s):
        return result

    balance = {}
    nonzero = 0
    for ch in p:
        nonzero = adjust(balance, ch, +1, nonzero)

    for right in range(len(s)):
        nonzero = adjust(balance, s[right], -1, nonzero)        # letter enters
        if right >= k:
            nonzero = adjust(balance, s[right - k], +1, nonzero)  # letter leaves
        if right >= k - 1 and nonzero == 0:
            result.append(right - k + 1)

    return result


if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))   # [0, 6]
    print(find_anagrams("abab", "ab"))          # [0, 1, 2]
