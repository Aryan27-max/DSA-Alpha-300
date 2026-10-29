# ============================================================
# Day 22 - VARIANT: Longest Valid Parentheses  (LeetCode 32 - Hard)
# ============================================================
# The question:
#   s has only '(' and ')'. Return the length of the longest substring
#   that is a valid (well-formed) parentheses string.
#
#   Example: "(()" -> 2      ")()())" -> 4      "" -> 0
#
# The big idea (stack of INDEXES):
#   Push indexes instead of characters, so we can measure lengths.
#   Keep a "floor" at the bottom of the stack: the index just BEFORE the
#   current valid stretch could begin. Start with -1.
#   - '(' : push its index.
#   - ')' : pop.
#       * If the stack is now empty, this ')' can't be matched - it becomes
#         the new floor (push its index).
#       * Otherwise a valid stretch ends here and starts right after the
#         new top: length = i - stack[-1].
#
# Bonus O(1)-space version: count opens/closes left->right (reset when
# closes > opens), then right->left (reset when opens > closes).
# ============================================================


def longest_valid_parentheses_brute(s):
    # Brute force: from every start, extend while the balance never drops below 0.
    best = 0
    n = len(s)
    for i in range(n):
        balance = 0
        for j in range(i, n):
            balance += 1 if s[j] == "(" else -1
            if balance < 0:
                break                       # can't recover from too many ')'
            if balance == 0 and j - i + 1 > best:
                best = j - i + 1
    return best


def longest_valid_parentheses(s):
    stack = [-1]                    # floor: just before where a valid run can start
    best = 0

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)     # unmatched ')' -> new floor
            else:
                length = i - stack[-1]
                if length > best:
                    best = length

    return best


def longest_valid_parentheses_o1(s):
    best = 0
    opens = closes = 0
    for ch in s:                                    # left -> right
        if ch == "(":
            opens += 1
        else:
            closes += 1
        if opens == closes and 2 * closes > best:
            best = 2 * closes
        elif closes > opens:
            opens = closes = 0                      # too many ')' - start over
    opens = closes = 0
    for i in range(len(s) - 1, -1, -1):             # right -> left
        if s[i] == "(":
            opens += 1
        else:
            closes += 1
        if opens == closes and 2 * opens > best:
            best = 2 * opens
        elif opens > closes:
            opens = closes = 0                      # too many '(' - start over
    return best


if __name__ == "__main__":
    print(longest_valid_parentheses("(()"))        # 2
    print(longest_valid_parentheses(")()())"))     # 4
    print(longest_valid_parentheses(""))           # 0
    print(longest_valid_parentheses("()(())"))     # 6
    print(longest_valid_parentheses_o1(")()())"))  # 4
