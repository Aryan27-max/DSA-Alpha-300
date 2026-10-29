# ============================================================
# Day 23 - VARIANT: Remove All Adjacent Duplicates In String  (LeetCode 1047)
# ============================================================
# The question:
#   Keep removing two equal letters that sit next to each other until
#   you can't anymore. Return the final string.
#
#   Example: "abbaca" -> "ca"
#            "abbaca" -> remove "bb" -> "aaca" -> remove "aa" -> "ca"
#
# The big idea:
#   Exactly Make The String Great with a simpler "bad pair" test:
#   same letter. Top of stack equals the new letter -> pop; else push.
# ============================================================


def remove_duplicates_brute(s):
    # Brute force: find the first adjacent pair, cut it, repeat.
    chars = list(s)
    changed = True
    while changed:
        changed = False
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                chars.pop(i + 1)
                chars.pop(i)
                changed = True
                break
    return "".join(chars)


def remove_duplicates(s):
    stack = []
    for ch in s:
        if len(stack) > 0 and stack[-1] == ch:
            stack.pop()             # twins cancel
        else:
            stack.append(ch)
    return "".join(stack)


if __name__ == "__main__":
    print(remove_duplicates("abbaca"))         # ca
    print(remove_duplicates("azxxzy"))         # ay
    print(remove_duplicates_brute("abbaca"))   # ca
