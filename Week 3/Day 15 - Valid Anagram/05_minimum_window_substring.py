# ============================================================
# Day 15 - VARIANT: Minimum Window Substring  (LeetCode 76 - Hard)
# ============================================================
# The question:
#   Find the SHORTEST substring of s that contains every character of t
#   (including duplicates). Return "" if there isn't one.
#
#   Example: s = "ADOBECODEBANC", t = "ABC" -> "BANC"
#
# The big idea (target-cover window):
#   need[ch] = how many of ch we still need. 'missing' = total still needed.
#   1. Grow right. If the new char was still needed, missing -= 1.
#   2. When missing == 0 the window covers t. Now shrink from the left
#      as far as possible, recording the smallest window. The moment we
#      drop a char that was actually needed, missing goes back up and we
#      go back to growing.
#   Each character enters and leaves once -> O(|s| + |t|).
# ============================================================


def covers(window_count, need_count):
    for ch in need_count:
        if window_count.get(ch, 0) < need_count[ch]:
            return False
    return True


def min_window_brute(s, t):
    # Brute force: try every start, grow until it covers t.
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    best = ""
    for i in range(len(s)):
        have = {}
        for j in range(i, len(s)):
            have[s[j]] = have.get(s[j], 0) + 1
            if covers(have, need):
                if best == "" or j - i + 1 < len(best):
                    best = s[i:j + 1]
                break
    return best


def min_window(s, t):
    if len(t) == 0 or len(t) > len(s):
        return ""

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)

    left = 0
    best_start, best_len = 0, len(s) + 1

    for right in range(len(s)):
        ch = s[right]
        if need.get(ch, 0) > 0:
            missing -= 1                    # this char was actually needed
        need[ch] = need.get(ch, 0) - 1      # negative = we have extras

        while missing == 0:                 # window covers t -> try to shrink
            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1
            out = s[left]
            need[out] += 1
            if need[out] > 0:
                missing += 1                # we just lost a needed char
            left += 1

    if best_len == len(s) + 1:
        return ""
    return s[best_start:best_start + best_len]


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))   # BANC
    print(min_window("a", "a"))                 # a
    print(min_window("a", "aa"))                # (empty string)
