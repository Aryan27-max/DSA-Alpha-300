# ============================================================
# Day 16 - VARIANT: Find the Difference  (LeetCode 389)
# ============================================================
# The question:
#   t is s shuffled, plus ONE extra letter. Return that extra letter.
#
#   Example: s = "abcd", t = "abcde" -> "e"
#
# The big idea (two bags, find the odd one out):
#   Day 3 solved this with XOR. Today's angle is the frequency map:
#   put s's letters in a "bag" (dict of counts). Then take t's letters
#   out of the bag one by one. The first letter you can't take out is
#   the extra one.
# ============================================================


def find_the_difference_brute(s, t):
    # Brute force: for each letter in t, compare how many times it appears in each.
    for ch in t:
        in_s = 0
        for c in s:
            if c == ch:
                in_s += 1
        in_t = 0
        for c in t:
            if c == ch:
                in_t += 1
        if in_t > in_s:
            return ch
    return ""


def find_the_difference(s, t):
    bag = {}
    for ch in s:
        bag[ch] = bag.get(ch, 0) + 1    # fill the bag with s's letters

    for ch in t:
        if bag.get(ch, 0) == 0:
            return ch                   # nothing left of this letter -> it's the extra
        bag[ch] -= 1                    # take one copy out

    return ""


if __name__ == "__main__":
    print(find_the_difference("abcd", "abcde"))   # e
    print(find_the_difference("", "y"))           # y
    print(find_the_difference("aab", "abaa"))     # a
