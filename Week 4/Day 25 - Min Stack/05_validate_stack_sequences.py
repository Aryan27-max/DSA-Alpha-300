# ============================================================
# Day 25 - VARIANT: Validate Stack Sequences  (LeetCode 946)
# ============================================================
# The question:
#   pushed and popped are two orderings of the same distinct numbers.
#   Could they be the result of pushes and pops on one empty stack?
#
#   Example: pushed = [1,2,3,4,5], popped = [4,5,3,2,1] -> True
#            pushed = [1,2,3,4,5], popped = [4,3,5,1,2] -> False
#
# The big idea (replay the sequence):
#   Actually run it. Push values in order. After every push, pop as long
#   as the stack's top is the next value we're supposed to pop.
#   At the end, if every value was popped, the sequence is valid.
#   Greedy popping is always safe: if the top is the one we need next,
#   waiting can only bury it.
#
#   O(1) extra space trick: reuse the 'pushed' list as the stack, with a
#   write pointer as its size (read/write pointers from Day 10).
# ============================================================


def validate_brute(pushed, popped):
    # Brute force: try every choice (push next / pop top) recursively.
    def go(i, j, stack):
        if j == len(popped):
            return True
        if len(stack) > 0 and stack[-1] == popped[j]:
            v = stack.pop()
            ok = go(i, j + 1, stack)
            stack.append(v)
            if ok:
                return True
        if i < len(pushed):
            stack.append(pushed[i])
            ok = go(i + 1, j, stack)
            stack.pop()
            return ok
        return False
    return go(0, 0, [])


def validate_stack_sequences(pushed, popped):
    stack = []
    j = 0                                   # next value we must pop
    for x in pushed:
        stack.append(x)
        while len(stack) > 0 and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)


def validate_stack_sequences_o1(pushed, popped):
    pushed = pushed[:]                      # copy so the caller's list isn't changed
    size = 0                                # pushed[0..size-1] is our stack
    j = 0
    for x in pushed:
        pushed[size] = x
        size += 1
        while size > 0 and pushed[size - 1] == popped[j]:
            size -= 1
            j += 1
    return size == 0


if __name__ == "__main__":
    print(validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))      # True
    print(validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))      # False
    print(validate_stack_sequences_o1([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))   # True
