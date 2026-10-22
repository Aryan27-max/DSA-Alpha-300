# ============================================================
# Day 15 - PRIMARY: Valid Anagram  (LeetCode 242)
# ============================================================
# The question:
#   Return True if t is an anagram of s - same letters, same number of
#   times each, just in a different order.
#
#   Example: s = "anagram", t = "nagaram" -> True
#            s = "rat",     t = "car"     -> False
#
# The big idea (character frequency counting):
#   Two strings are anagrams exactly when their letter COUNTS match.
#   Build two dicts by hand, then compare them key by key.
#   (No Counter(s) == Counter(t), no sorted(s) == sorted(t).)
#
#   Even better: ONE dict. Add 1 for every letter in s, subtract 1 for
#   every letter in t. If they're anagrams, everything ends at 0.
# ============================================================


def is_anagram_brute(s, t):
    # Brute force: for each letter of s, find and remove one matching letter in t.
    if len(s) != len(t):
        return False
    remaining = list(t)
    for ch in s:
        found = False
        for i in range(len(remaining)):
            if remaining[i] == ch:
                remaining.pop(i)        # use this copy up
                found = True
                break
        if not found:
            return False
    return True


def is_anagram_two_dicts(s, t):
    # Two dicts, compared by hand (the version the plan asks for).
    if len(s) != len(t):
        return False

    count_s = {}
    for ch in s:
        count_s[ch] = count_s.get(ch, 0) + 1
    count_t = {}
    for ch in t:
        count_t[ch] = count_t.get(ch, 0) + 1

    if len(count_s) != len(count_t):
        return False                    # different sets of letters
    for ch in count_s:
        if count_t.get(ch, 0) != count_s[ch]:
            return False                # same letter, different amount
    return True


def is_anagram(s, t):
    # One dict: +1 for s, -1 for t. Everything must cancel to zero.
    if len(s) != len(t):
        return False

    balance = {}
    for i in range(len(s)):
        balance[s[i]] = balance.get(s[i], 0) + 1
        balance[t[i]] = balance.get(t[i], 0) - 1

    for ch in balance:
        if balance[ch] != 0:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))            # True
    print(is_anagram("rat", "car"))                    # False
    print(is_anagram_two_dicts("listen", "silent"))    # True
    print(is_anagram_brute("aacc", "ccac"))            # False
