# ============================================================
# Day 22 - PRIMARY: Valid Parentheses  (LeetCode 20)
# ============================================================
# The question:
#   s only contains ( ) { } [ ]. Return True if:
#     - every opening bracket is closed by the SAME type of bracket, and
#     - brackets close in the right order (the last one opened closes first).
#
#   Example: "()[]{}" -> True     "(]" -> False     "([)]" -> False
#            "{[]}"   -> True
#
# The big idea (push open, pop and compare on close):
#   A stack is just a list where you only touch the END:
#     push = list.append(x)      pop = list.pop()      top = list[-1]
#   - See an opening bracket?  Push it - "I owe a closer for this".
#   - See a closing bracket?   The top of the stack MUST be its partner.
#     If the stack is empty or the top is the wrong type -> invalid.
#     Otherwise pop it - that debt is paid.
#   - At the end the stack must be empty (no unpaid openers).
#   The last opened bracket is always on top, which is exactly the
#   "last opened closes first" rule. That's what a stack IS.
#   (No collections.deque - a plain list is your stack.)
# ============================================================


def is_valid_brute(s):
    # Brute force: keep deleting "()", "[]", "{}" pairs until nothing changes.
    # A valid string shrinks all the way to "". Each round is O(n) and
    # there can be n/2 rounds -> O(n^2).
    while True:
        shorter = s.replace("()", "").replace("[]", "").replace("{}", "")
        if shorter == s:
            break
        s = shorter
    return s == ""


def is_valid(s):
    partner = {")": "(", "]": "[", "}": "{"}    # closer -> the opener it needs
    stack = []

    for ch in s:
        if ch in partner:                       # it's a closing bracket
            if len(stack) == 0 or stack[-1] != partner[ch]:
                return False                    # nothing to close, or wrong type
            stack.pop()                         # matched - pay off the debt
        else:
            stack.append(ch)                    # opening bracket - remember it

    return len(stack) == 0                      # leftover openers = invalid


if __name__ == "__main__":
    print(is_valid("()"))            # True
    print(is_valid("()[]{}"))        # True
    print(is_valid("(]"))            # False
    print(is_valid("([)]"))          # False
    print(is_valid("{[]}"))          # True
    print(is_valid("(("))            # False
    print(is_valid_brute("{[]}"))    # True
