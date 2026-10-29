# ============================================================
# Day 22 - VARIANT: Minimum Add to Make Parentheses Valid  (LeetCode 921)
# ============================================================
# The question:
#   s has only '(' and ')'. In one move you can INSERT a parenthesis
#   anywhere. Return the fewest moves to make s valid.
#
#   Example: "())" -> 1      "(((" -> 3      "()))((" -> 4
#
# The big idea (insert to make valid):
#   Stack version: push '(' ; on ')' pop a matching '(' if there is one,
#   otherwise this ')' is unmatched. Everything left over is unmatched,
#   and each unmatched bracket needs exactly one insert.
#
#   With only ONE bracket type, the stack only ever holds '(' - so we
#   don't need the stack itself, just its SIZE:
#     open_count  = '(' still waiting for a ')'
#     close_needed = ')' that had no '(' to match (each needs an inserted '(')
#   Answer = open_count + close_needed. O(1) space.
# ============================================================


def min_add_to_make_valid_stack(s):
    # Stack version: whatever is left unmatched must be fixed with an insert.
    stack = []
    for ch in s:
        if ch == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop()                 # this ')' closes a waiting '('
        else:
            stack.append(ch)            # unmatched (either kind)
    return len(stack)


def min_add_to_make_valid(s):
    open_count = 0                      # '(' still waiting to be closed
    close_needed = 0                    # ')' with nothing to close

    for ch in s:
        if ch == "(":
            open_count += 1
        elif open_count > 0:
            open_count -= 1             # matched a waiting '('
        else:
            close_needed += 1           # we'll have to insert a '(' before it

    return open_count + close_needed


if __name__ == "__main__":
    print(min_add_to_make_valid("())"))       # 1
    print(min_add_to_make_valid("((("))       # 3
    print(min_add_to_make_valid("()))(("))    # 4
    print(min_add_to_make_valid_stack("()))((")) # 4
