# ============================================================
# Day 19 - VARIANT: Rotate String  (LeetCode 796)
# ============================================================
# The question:
#   Return True if shifting s left some number of times gives goal.
#
#   Example: "abcde", "cdeab" -> True       "abcde", "abced" -> False
#
# Day 17 vs Day 19 - the "index mapping" view:
#   Day 17 searched for goal inside s + s with KMP.
#   Today, think of a rotation as an index mapping:
#       goal[i] must equal s[(i + k) % n]   for one fixed shift k.
#   Only shifts where s[k] == goal[0] are worth trying, so we skip the
#   rest immediately. Simple, no extra string, O(1) space.
#   (Worst case is still O(n^2), e.g. "aaaa...ab" - KMP from Day 17 is
#   the guaranteed O(n) version.)
# ============================================================


def rotate_string_brute(s, goal):
    # Brute force: actually build each rotation as a new string.
    if len(s) != len(goal):
        return False
    if s == goal:
        return True
    cur = s
    for _ in range(len(s)):
        cur = cur[1:] + cur[0]          # one left shift
        if cur == goal:
            return True
    return False


def rotate_string(s, goal):
    n = len(s)
    if n != len(goal):
        return False
    if n == 0:
        return True

    for k in range(n):
        if s[k] != goal[0]:
            continue                    # this shift can't even match the first char
        ok = True
        for i in range(n):
            if s[(i + k) % n] != goal[i]:
                ok = False
                break
        if ok:
            return True
    return False


if __name__ == "__main__":
    print(rotate_string("abcde", "cdeab"))   # True
    print(rotate_string("abcde", "abced"))   # False
    print(rotate_string("", ""))             # True
