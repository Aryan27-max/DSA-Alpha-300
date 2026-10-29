# ============================================================
# Day 22 - VARIANT: Remove Outermost Parentheses  (LeetCode 1021)
# ============================================================
# The question:
#   s is a valid parentheses string. Split it into "primitive" pieces
#   (the smallest non-empty valid chunks that can't be split further),
#   and remove the outermost pair from EACH piece.
#
#   Example: "(()())(())" -> "()()()"
#            pieces: "(()())" + "(())"  ->  "()()" + "()"
#
# The big idea (strip the outer layer with a depth counter):
#   Think of the stack's SIZE as "depth".
#   - '(' at depth 0 is an outermost opener -> skip it.
#   - ')' that brings depth back to 0 is an outermost closer -> skip it.
#   - Everything else is kept.
#   Order matters: for '(' check depth BEFORE going deeper; for ')'
#   check depth AFTER coming back up.
# ============================================================


def remove_outer_parentheses_brute(s):
    # Brute force: find each primitive piece, then copy its inside.
    result = []
    depth = 0
    start = 0
    for i in range(len(s)):
        depth += 1 if s[i] == "(" else -1
        if depth == 0:                      # a primitive piece is s[start..i]
            for j in range(start + 1, i):   # copy everything except its two ends
                result.append(s[j])
            start = i + 1
    return "".join(result)


def remove_outer_parentheses(s):
    result = []
    depth = 0

    for ch in s:
        if ch == "(":
            if depth > 0:
                result.append(ch)       # not outermost -> keep
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                result.append(ch)       # not the closer of a piece -> keep

    return "".join(result)


if __name__ == "__main__":
    print(remove_outer_parentheses("(()())(())"))           # ()()()
    print(remove_outer_parentheses("(()())(())(()(()))"))   # ()()()()(())
    print(remove_outer_parentheses("()()"))                 # (empty)
