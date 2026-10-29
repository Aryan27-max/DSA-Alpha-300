# ============================================================
# Day 23 - VARIANT: Backspace String Compare  (LeetCode 844)
# ============================================================
# The question:
#   s and t are typed into a text editor; '#' means backspace.
#   Return True if they end up as the same text.
#   (Backspace on an empty editor does nothing.)
#
#   Example: s = "ab#c", t = "ad#c" -> True  (both "ac")
#            s = "a#c",  t = "b"    -> False
#
# The big idea (delete + apply backspace with a stack):
#   Typing a letter = push. Backspace = pop (if there's anything).
#   Build both final texts this way, then compare them.
#   (Day 31 comes back to this and solves it with O(1) extra space.)
# ============================================================


def build_brute(s):
    # Brute force: keep a real string and slice off the last char on '#'.
    # Each slice copies the whole string -> O(n^2).
    text = ""
    for ch in s:
        if ch == "#":
            text = text[:-1]
        else:
            text = text + ch
    return text


def backspace_compare_brute(s, t):
    return build_brute(s) == build_brute(t)


def build(s):
    stack = []
    for ch in s:
        if ch == "#":
            if len(stack) > 0:
                stack.pop()         # backspace removes the last typed char
        else:
            stack.append(ch)        # typing a char
    return stack


def backspace_compare(s, t):
    a = build(s)
    b = build(t)
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


if __name__ == "__main__":
    print(backspace_compare("ab#c", "ad#c"))         # True
    print(backspace_compare("ab##", "c#d#"))         # True
    print(backspace_compare("a#c", "b"))             # False
    print(backspace_compare_brute("a##c", "#a#c"))   # True
