# ============================================================
# Day 19 - VARIANT: Buddy Strings  (LeetCode 859)
# ============================================================
# The question:
#   Can you swap exactly one pair of positions in s to get goal?
#
#   Example: "ab","ba" -> True    "ab","ab" -> False    "aa","aa" -> True
#
# Day 17 vs Day 19 - the "mapping" view:
#   Write down every position where s and goal differ as a pair
#   (s_char -> goal_char). One swap of positions i and j makes the
#   pairs (x -> y) and (y -> x) - a mapping that goes both ways, just
#   like today's primary. So:
#     - exactly two mismatched pairs, and the second is the first flipped
#     - OR no mismatches, but some letter repeats (swap the twins)
# ============================================================


def buddy_strings_brute(s, goal):
    # Brute force: try every swap.
    if len(s) != len(goal):
        return False
    c = list(s)
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            c[i], c[j] = c[j], c[i]
            if "".join(c) == goal:
                return True
            c[i], c[j] = c[j], c[i]
    return False


def buddy_strings(s, goal):
    if len(s) != len(goal):
        return False

    pairs = []                          # mismatched (s_char, goal_char) pairs
    letter_count = {}
    for i in range(len(s)):
        letter_count[s[i]] = letter_count.get(s[i], 0) + 1
        if s[i] != goal[i]:
            pairs.append((s[i], goal[i]))
            if len(pairs) > 2:
                return False

    if len(pairs) == 0:
        for ch in letter_count:
            if letter_count[ch] >= 2:
                return True             # swap two copies of the same letter
        return False

    if len(pairs) == 2:
        (x1, y1), (x2, y2) = pairs
        return x1 == y2 and y1 == x2    # (x -> y) and (y -> x)

    return False


if __name__ == "__main__":
    print(buddy_strings("ab", "ba"))      # True
    print(buddy_strings("ab", "ab"))      # False
    print(buddy_strings("aa", "aa"))      # True
    print(buddy_strings("abcd", "badc"))  # False
