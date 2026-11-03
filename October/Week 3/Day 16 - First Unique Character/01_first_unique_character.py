# ============================================================
# Day 16 - PRIMARY: First Unique Character in a String  (LeetCode 387)
# ============================================================
# The question:
#   Return the index of the first character that appears only once in s.
#   If there isn't one, return -1.
#
#   Example: "leetcode" -> 0       "loveleetcode" -> 2       "aabb" -> -1
#
# The big idea (count first, then scan in order):
#   Pass 1: count every character in a plain dict.
#   Pass 2: walk s from the left again; the first character whose count
#           is 1 is the answer.
#   The second pass walks the STRING (not the dict) - that's what keeps
#   the original order. (No Counter, no OrderedDict.)
# ============================================================


def first_uniq_char_brute(s):
    # Brute force: for each character, scan the whole string for a copy.
    n = len(s)
    for i in range(n):
        unique = True
        for j in range(n):
            if i != j and s[i] == s[j]:
                unique = False
                break
        if unique:
            return i
    return -1


def first_uniq_char(s):
    counts = {}
    for ch in s:                        # pass 1: build the map
        counts[ch] = counts.get(ch, 0) + 1

    for i in range(len(s)):             # pass 2: query it in string order
        if counts[s[i]] == 1:
            return i

    return -1


if __name__ == "__main__":
    print(first_uniq_char("leetcode"))          # 0
    print(first_uniq_char("loveleetcode"))      # 2
    print(first_uniq_char("aabb"))              # -1
    print(first_uniq_char_brute("loveleetcode"))  # 2
