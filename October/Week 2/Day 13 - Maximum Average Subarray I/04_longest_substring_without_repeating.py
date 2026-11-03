# ============================================================
# Day 13 - VARIANT: Longest Substring Without Repeating Characters  (LeetCode 3)
# ============================================================
# The question:
#   Find the length of the longest substring with no repeated characters.
#
#   Example: "abcabcbb" -> 3 ("abc")     "bbbbb" -> 1     "pwwkew" -> 3 ("wke")
#
# The big idea (variable window + last-seen dict):
#   Keep a window [left, right] with all-distinct characters.
#   Remember the last index of every character (dict).
#   When s[right] was already seen INSIDE the window, jump left to just
#   after that old position - that kicks the duplicate out in one move.
# ============================================================


def length_of_longest_substring_brute(s):
    # Brute force: from each start, grow until a character repeats.
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            if j - i + 1 > best:
                best = j - i + 1
    return best


def length_of_longest_substring(s):
    last_seen = {}                          # char -> last index we saw it at
    left = 0
    best = 0

    for right in range(len(s)):
        ch = s[right]
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1        # duplicate inside the window -> jump past it

        last_seen[ch] = right
        if right - left + 1 > best:
            best = right - left + 1

    return best


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))   # 3
    print(length_of_longest_substring("bbbbb"))      # 1
    print(length_of_longest_substring("pwwkew"))     # 3
    print(length_of_longest_substring("abba"))       # 2
