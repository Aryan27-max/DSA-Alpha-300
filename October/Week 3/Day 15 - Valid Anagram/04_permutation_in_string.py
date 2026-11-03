# ============================================================
# Day 15 - VARIANT: Permutation in String  (LeetCode 567)
# ============================================================
# The question:
#   Does s2 contain some rearrangement of s1 as a contiguous substring?
#
#   Example: s1 = "ab", s2 = "eidbaooo" -> True ("ba")
#
# The big idea:
#   "A permutation of s1" is just "an anagram of s1". So this is Find All
#   Anagrams, but we can stop at the FIRST hit. Here we use two 26-slot
#   count lists and compare them directly - comparing 26 numbers is O(1).
# ============================================================


def check_inclusion_brute(s1, s2):
    # Brute force: count every window from scratch.
    k = len(s1)
    need = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1
    for i in range(len(s2) - k + 1):
        have = [0] * 26
        for j in range(i, i + k):
            have[ord(s2[j]) - 97] += 1
        if have == need:
            return True
    return False


def check_inclusion(s1, s2):
    k = len(s1)
    if k > len(s2):
        return False

    need = [0] * 26
    have = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1

    for right in range(len(s2)):
        have[ord(s2[right]) - 97] += 1          # letter enters
        if right >= k:
            have[ord(s2[right - k]) - 97] -= 1  # letter leaves
        if have == need:                        # 26 comparisons = constant time
            return True

    return False


if __name__ == "__main__":
    print(check_inclusion("ab", "eidbaooo"))   # True
    print(check_inclusion("ab", "eidboaoo"))   # False
