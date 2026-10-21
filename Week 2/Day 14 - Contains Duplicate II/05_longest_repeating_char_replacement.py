# ============================================================
# Day 14 - VARIANT: Longest Repeating Character Replacement  (LeetCode 424)
# ============================================================
# The question:
#   Uppercase string s. You can change at most k characters to any other
#   letter. Return the length of the longest substring that can be made
#   into ONE repeated letter.
#
#   Example: s = "ABAB", k = 2 -> 4      s = "AABABBA", k = 1 -> 4
#
# The big idea (frequency window):
#   In a window, keep the most common letter and change the rest.
#   Changes needed = window length - count of the most common letter.
#   If that's > k, the window is invalid -> slide left forward.
#   Trick: we never LOWER max_freq when shrinking. A stale max_freq can
#   only stop the window from growing - it never gives a wrong bigger
#   answer, because the answer only improves when a real higher
#   frequency appears.
# ============================================================


def character_replacement_brute(s, k):
    # Brute force: every start, grow while changes needed <= k.
    best = 0
    n = len(s)
    for i in range(n):
        counts = {}
        top = 0
        for j in range(i, n):
            counts[s[j]] = counts.get(s[j], 0) + 1
            if counts[s[j]] > top:
                top = counts[s[j]]
            if (j - i + 1) - top <= k:
                if j - i + 1 > best:
                    best = j - i + 1
    return best


def character_replacement(s, k):
    counts = {}
    left = 0
    max_freq = 0
    best = 0

    for right in range(len(s)):
        ch = s[right]
        counts[ch] = counts.get(ch, 0) + 1
        if counts[ch] > max_freq:
            max_freq = counts[ch]           # most common letter count so far

        window_len = right - left + 1
        if window_len - max_freq > k:       # too many letters to change
            counts[s[left]] -= 1
            left += 1                       # slide (window length stays the same)

        if right - left + 1 > best:
            best = right - left + 1

    return best


if __name__ == "__main__":
    print(character_replacement("ABAB", 2))          # 4
    print(character_replacement("AABABBA", 1))       # 4
    print(character_replacement_brute("AABABBA", 1)) # 4
