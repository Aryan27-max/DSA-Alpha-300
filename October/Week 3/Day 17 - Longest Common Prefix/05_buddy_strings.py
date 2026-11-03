# ============================================================
# Day 17 - VARIANT: Buddy Strings  (LeetCode 859)
# ============================================================
# The question:
#   Return True if you can swap EXACTLY ONE pair of letters in s
#   (two different positions) to make it equal to goal.
#
#   Example: "ab", "ba" -> True       "ab", "ab" -> False
#            "aa", "aa" -> True (swap the two a's - nothing changes)
#
# The big idea (char-by-char compare):
#   Walk both strings by index and collect the positions where they differ.
#   - Different lengths -> False.
#   - Exactly 2 differences, and they're "crossed" (s[i]==goal[j] and
#     s[j]==goal[i]) -> True.
#   - 0 differences -> only True if s has some repeated letter (swap the
#     two copies and nothing changes).
#   - Anything else -> False.
# ============================================================


def buddy_strings_brute(s, goal):
    # Brute force: actually try every swap.
    if len(s) != len(goal):
        return False
    chars = list(s)
    n = len(chars)
    for i in range(n):
        for j in range(i + 1, n):
            chars[i], chars[j] = chars[j], chars[i]
            if "".join(chars) == goal:
                return True
            chars[i], chars[j] = chars[j], chars[i]   # undo
    return False


def buddy_strings(s, goal):
    if len(s) != len(goal):
        return False

    diffs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diffs.append(i)
            if len(diffs) > 2:
                return False                # too many differences for one swap

    if len(diffs) == 2:
        i, j = diffs
        return s[i] == goal[j] and s[j] == goal[i]

    if len(diffs) == 0:
        seen = set()
        for ch in s:
            if ch in seen:
                return True                 # swap two identical letters
            seen.add(ch)
        return False

    return False                            # exactly 1 difference can't be fixed by a swap


if __name__ == "__main__":
    print(buddy_strings("ab", "ba"))          # True
    print(buddy_strings("ab", "ab"))          # False
    print(buddy_strings("aa", "aa"))          # True
    print(buddy_strings("abcaa", "abcbb"))    # False
