# ============================================================
# Day 23 - VARIANT: Build an Array With Stack Operations  (LeetCode 1441)
# ============================================================
# The question:
#   You read numbers 1, 2, 3, ..., n in order. For each one you can
#   "Push" it onto a stack, and you can "Pop" the top. Return the list of
#   operations that makes the stack equal to target (strictly increasing).
#   Stop as soon as the stack equals target.
#
#   Example: target = [1,3], n = 3 -> ["Push","Push","Pop","Push"]
#            (push 1, push 2, pop 2, push 3)
#
# The big idea (build via stack ops):
#   Every number you read must be pushed first (that's the only way to
#   read it). If it's in target, keep it. If not, pop it straight away.
#   Since target is increasing, just walk a pointer through target.
#   We don't even need a real stack - only the list of operations.
# ============================================================


def build_array_simulated(target, n):
    # Version with a real stack, checking it against target as we go.
    ops = []
    stack = []
    for num in range(1, n + 1):
        if len(stack) == len(target):
            break                       # already built
        stack.append(num)
        ops.append("Push")
        if stack[-1] != target[len(stack) - 1]:
            stack.pop()                 # not wanted -> throw it away
            ops.append("Pop")
    return ops


def build_array(target, n):
    ops = []
    j = 0                               # next value of target we need
    for num in range(1, n + 1):
        if j == len(target):
            break
        ops.append("Push")
        if num == target[j]:
            j += 1                      # keep it
        else:
            ops.append("Pop")           # skip it
    return ops


if __name__ == "__main__":
    print(build_array([1, 3], 3))       # ['Push', 'Push', 'Pop', 'Push']
    print(build_array([1, 2, 3], 3))    # ['Push', 'Push', 'Push']
    print(build_array([1, 2], 4))       # ['Push', 'Push']
