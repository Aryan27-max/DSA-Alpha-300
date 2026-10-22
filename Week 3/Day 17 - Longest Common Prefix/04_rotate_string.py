# ============================================================
# Day 17 - VARIANT: Rotate String  (LeetCode 796)
# ============================================================
# The question:
#   A "shift" moves the first character of s to the end.
#   Return True if some number of shifts turns s into goal.
#
#   Example: s = "abcde", goal = "cdeab" -> True
#            s = "abcde", goal = "abced" -> False
#
# The big idea:
#   Every rotation of s appears inside s + s.
#     "abcde" + "abcde" = "abcdeabcde" contains "cdeab".
#   So: same length AND goal is a substring of s + s.
#   For the substring check we write KMP ourselves (no 'in' shortcut):
#   build an LPS table for goal ("longest prefix that's also a suffix"),
#   then scan s + s without ever moving backwards. O(n).
# ============================================================


def rotate_string_brute(s, goal):
    # Brute force: try every shift and compare char by char.
    n = len(s)
    if n != len(goal):
        return False
    if n == 0:
        return True
    for shift in range(n):
        ok = True
        for i in range(n):
            if s[(i + shift) % n] != goal[i]:
                ok = False
                break
        if ok:
            return True
    return False


def build_lps(pattern):
    # lps[i] = length of the longest proper prefix of pattern[0..i]
    #          that is also a suffix of it.
    lps = [0] * len(pattern)
    length = 0                          # current matched prefix length
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]    # fall back to a shorter prefix, don't move i
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_contains(text, pattern):
    if len(pattern) == 0:
        return True
    lps = build_lps(pattern)
    j = 0                               # how much of pattern is matched
    for ch in text:
        while j > 0 and ch != pattern[j]:
            j = lps[j - 1]              # reuse what we already matched
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
    return False


def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    return kmp_contains(s + s, goal)


if __name__ == "__main__":
    print(rotate_string("abcde", "cdeab"))         # True
    print(rotate_string("abcde", "abced"))         # False
    print(rotate_string_brute("aa", "a"))          # False
