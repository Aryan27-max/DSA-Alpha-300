# ============================================================
# Day 22 - VARIANT: Minimum Remove to Make Valid Parentheses  (LeetCode 1249)
# ============================================================
# The question:
#   s has letters and '(' ')'. Remove the FEWEST parentheses so the
#   result is valid. Return any valid answer.
#
#   Example: "lee(t(c)o)de)" -> "lee(t(c)o)de"
#            "a)b(c)d"       -> "ab(c)d"
#            "))(("          -> ""
#
# The big idea (deletion with a stack of indexes):
#   - '(' : push its index (waiting for a partner).
#   - ')' : if the stack has a waiting '(', pop it (matched).
#           Otherwise this ')' has no partner -> mark it for removal.
#   - At the end, every index still in the stack is a '(' that never got
#     closed -> mark those too.
#   Build the answer skipping marked positions. Each removal is forced,
#   so this is the minimum.
# ============================================================


def is_valid(s):
    depth = 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def min_remove_brute(s):
    # Brute force (BFS): remove 0 chars, then 1, then 2 ... and return the
    # first valid string found. Exponential - only for tiny inputs.
    level = [s]
    seen = {s}
    while True:
        for cand in level:
            if is_valid(cand):
                return cand
        next_level = []
        for cand in level:
            for i in range(len(cand)):
                if cand[i] == "(" or cand[i] == ")":
                    shorter = cand[:i] + cand[i + 1:]
                    if shorter not in seen:
                        seen.add(shorter)
                        next_level.append(shorter)
        level = next_level


def min_remove_to_make_valid(s):
    remove = [False] * len(s)
    stack = []                          # indexes of '(' still waiting

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if len(stack) > 0:
                stack.pop()             # matched
            else:
                remove[i] = True        # ')' with no partner

    for i in stack:
        remove[i] = True                # '(' that never got closed

    result = []
    for i in range(len(s)):
        if not remove[i]:
            result.append(s[i])
    return "".join(result)


if __name__ == "__main__":
    print(min_remove_to_make_valid("lee(t(c)o)de)"))   # lee(t(c)o)de
    print(min_remove_to_make_valid("a)b(c)d"))         # ab(c)d
    print(min_remove_to_make_valid("))(("))            # (empty)
    print(min_remove_brute("a)b(c)d"))                 # ab(c)d
