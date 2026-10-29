# ============================================================
# Day 23 - VARIANT: Make The String Great  (LeetCode 1544)
# ============================================================
# The question:
#   A string is "bad" if two neighbours are the same letter in different
#   cases (like "aA" or "Bb"). Keep removing such pairs until none are
#   left. Return the result.
#
#   Example: "leEeetcode" -> "leetcode"
#            "abBAcC"     -> ""   (bB goes, then aA, then cC)
#
# The big idea (collapse adjacent pairs with a stack):
#   Removing a pair can make two NEW letters neighbours ("abBA" -> "aA").
#   A stack handles that for free: the top of the stack is always the
#   letter that is currently to the left of where we're reading.
#   - If the new letter and the top are a bad pair -> pop (both vanish).
#   - Otherwise push.
#   Same letter, different case = their ASCII codes differ by exactly 32.
# ============================================================


def is_bad_pair(a, b):
    return a != b and (ord(a) - ord(b) == 32 or ord(b) - ord(a) == 32)


def make_good_brute(s):
    # Brute force: scan for the first bad pair, cut it out, start over.
    chars = list(s)
    changed = True
    while changed:
        changed = False
        for i in range(len(chars) - 1):
            if is_bad_pair(chars[i], chars[i + 1]):
                chars.pop(i + 1)
                chars.pop(i)
                changed = True
                break
    return "".join(chars)


def make_good(s):
    stack = []
    for ch in s:
        if len(stack) > 0 and is_bad_pair(stack[-1], ch):
            stack.pop()                 # they cancel each other
        else:
            stack.append(ch)
    return "".join(stack)


if __name__ == "__main__":
    print(make_good("leEeetcode"))     # leetcode
    print(make_good("abBAcC"))         # (empty)
    print(make_good("s"))              # s
    print(make_good_brute("abBAcC"))   # (empty)
