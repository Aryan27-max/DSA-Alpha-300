# ============================================================
# Day 14 - VARIANT: Permutation in String  (LeetCode 567)
# ============================================================
# The question:
#   Return True if s2 contains any permutation of s1 as a substring
#   (some rearrangement of s1 appears in s2, letters next to each other).
#
#   Example: s1 = "ab", s2 = "eidbaooo" -> True  ("ba")
#            s1 = "ab", s2 = "eidboaoo" -> False
#
# The big idea (window + hashmap of counts):
#   A window of size len(s1) slides over s2. Keep a dict 'need' with the
#   letters of s1 and a counter 'missing' = letters still needed.
#   - A letter enters: if need[ch] > 0, it was useful -> missing -= 1.
#     Then need[ch] -= 1 (can go negative = "extra" copies).
#   - A letter leaves: need[ch] += 1; if that makes it > 0, we lost a
#     useful letter -> missing += 1.
#   missing == 0 means the window is a permutation of s1.
# ============================================================


def check_inclusion_brute(s1, s2):
    # Brute force: for every window, count letters and compare dicts.
    def count(text, start, length):
        c = {}
        for i in range(start, start + length):
            c[text[i]] = c.get(text[i], 0) + 1
        return c

    k = len(s1)
    target = count(s1, 0, k)
    for i in range(len(s2) - k + 1):
        if count(s2, i, k) == target:
            return True
    return False


def check_inclusion(s1, s2):
    k = len(s1)
    if k > len(s2):
        return False

    need = {}
    for ch in s1:
        need[ch] = need.get(ch, 0) + 1
    missing = k                             # letters still needed to complete s1

    for right in range(len(s2)):
        ch = s2[right]
        if need.get(ch, 0) > 0:
            missing -= 1                    # this letter fills a real need
        need[ch] = need.get(ch, 0) - 1

        if right >= k:                      # window too long -> drop the left letter
            out = s2[right - k]
            need[out] += 1
            if need[out] > 0:
                missing += 1                # we just lost a needed letter

        if missing == 0:
            return True

    return False


if __name__ == "__main__":
    print(check_inclusion("ab", "eidbaooo"))         # True
    print(check_inclusion("ab", "eidboaoo"))         # False
    print(check_inclusion("adc", "dcda"))            # True
    print(check_inclusion_brute("ab", "eidbaooo"))   # True
