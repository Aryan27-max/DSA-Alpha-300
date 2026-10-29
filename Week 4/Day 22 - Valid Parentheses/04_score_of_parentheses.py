# ============================================================
# Day 22 - VARIANT: Score of Parentheses  (LeetCode 856)
# ============================================================
# The question:
#   s is a balanced parentheses string. Its score is:
#     "()"        -> 1
#     AB (two balanced strings side by side) -> score(A) + score(B)
#     "(A)"       -> 2 * score(A)
#
#   Example: "()" -> 1    "(())" -> 2    "()()" -> 2    "(()(()))" -> 6
#
# The big idea (scored nesting with a stack):
#   Each stack slot holds the running score of one nesting level.
#   - '(' : open a new level with score 0.
#   - ')' : close the top level. If its score is 0 it was "()" -> worth 1,
#           otherwise it was "(A)" -> worth 2 * score.
#           Add that to the level underneath (the "AB" rule).
#   The bottom slot collects the final answer.
#
# Bonus O(1)-space trick:
#   Only the "()" pairs actually create points. A "()" sitting at depth d
#   (number of open brackets around it) is doubled d times -> 2^d.
#   So just add 2^depth every time you see "()".
# ============================================================


def score_brute(s):
    # Brute force (recursion): split into top-level pieces, score each one.
    total = 0
    depth = 0
    start = 0
    for i in range(len(s)):
        depth += 1 if s[i] == "(" else -1
        if depth == 0:                          # piece s[start..i]
            if i == start + 1:
                total += 1                      # it's "()"
            else:
                total += 2 * score_brute(s[start + 1:i])   # "(A)"
            start = i + 1
    return total


def score_of_parentheses(s):
    stack = [0]                     # bottom slot = score of the whole string

    for ch in s:
        if ch == "(":
            stack.append(0)         # new nesting level, nothing scored yet
        else:
            inner = stack.pop()
            if inner == 0:
                worth = 1           # "()"
            else:
                worth = 2 * inner   # "(A)"
            stack[-1] += worth      # add to the enclosing level

    return stack[0]


def score_of_parentheses_o1(s):
    total = 0
    depth = 0
    for i in range(len(s)):
        if s[i] == "(":
            depth += 1
        else:
            depth -= 1
            if s[i - 1] == "(":     # this ')' closes a "()" pair
                total += 2 ** depth
    return total


if __name__ == "__main__":
    print(score_of_parentheses("()"))          # 1
    print(score_of_parentheses("(())"))        # 2
    print(score_of_parentheses("()()"))        # 2
    print(score_of_parentheses("(()(()))"))    # 6
    print(score_of_parentheses_o1("(()(()))")) # 6
