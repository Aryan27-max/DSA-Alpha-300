# ============================================================
# Day 31 - PRIMARY: Backspace String Compare  (LeetCode 844)
# ============================================================
# The question:
#   s and t are typed into empty text editors. '#' is backspace
#   (backspace on an empty editor does nothing). Return True if both
#   editors end up showing the same text.
#
#   Example: s = "ab#c", t = "ad#c" -> True   (both "ac")
#            s = "a#c",  t = "b"    -> False
#
# Version 1 - two stacks (Day 23):
#   Typing = push, '#' = pop if not empty. Build both, compare.
#   O(n + m) time, O(n + m) space.
#
# Version 2 - BONUS, O(1) space with two reverse pointers:
#   Read both strings from the END. Going backwards, a '#' tells you to
#   SKIP the next real character you meet. So each pointer keeps a
#   'skip' counter:
#     '#'          -> skip += 1, move left
#     char, skip>0 -> this char was erased: skip -= 1, move left
#     char, skip=0 -> this char survives: stop here
#   Once both pointers rest on a surviving char (or ran off the start),
#   compare them. Different -> False. Same -> move both left and repeat.
#   No stacks, no new strings.
# ============================================================


def build(s):
    stack = []
    for ch in s:
        if ch == "#":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(ch)
    return stack


def backspace_compare_stacks(s, t):
    a, b = build(s), build(t)
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def next_survivor(s, i):
    # From index i going left, return the index of the next char that
    # survives the backspaces (or -1 if none).
    skip = 0
    while i >= 0:
        if s[i] == "#":
            skip += 1
        elif skip > 0:
            skip -= 1               # this char is erased
        else:
            return i                # this char survives
        i -= 1
    return -1


def backspace_compare(s, t):
    i, j = len(s) - 1, len(t) - 1
    while True:
        i = next_survivor(s, i)
        j = next_survivor(t, j)
        if i < 0 or j < 0:
            return i < 0 and j < 0  # both ran out at the same time?
        if s[i] != t[j]:
            return False
        i -= 1
        j -= 1


if __name__ == "__main__":
    print(backspace_compare("ab#c", "ad#c"))          # True
    print(backspace_compare("ab##", "c#d#"))          # True
    print(backspace_compare("a#c", "b"))              # False
    print(backspace_compare("bxj##tw", "bxo#j##tw"))  # True
    print(backspace_compare_stacks("a##c", "#a#c"))   # True
