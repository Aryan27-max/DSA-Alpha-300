# ============================================================
# Day 25 - VARIANT: Max Stack  (LeetCode 716 - Premium)
# ============================================================
# The question:
#   A stack that supports:
#     push(x), pop(), top(), peekMax(), popMax()
#   popMax removes the biggest element; if there's a tie, remove the one
#   closest to the top.
#
#   Example: push(5), push(1), push(5)
#            top() -> 5, popMax() -> 5, top() -> 1,
#            peekMax() -> 5, pop() -> 1, top() -> 5
#
# The big idea (Min Stack, flipped):
#   Keep 'maxes' alongside 'stack': maxes[i] = the max of stack[0..i].
#   (Here we push onto maxes EVERY time - simpler to keep in sync.)
#   push / pop / top / peekMax are all O(1).
#
#   popMax is the hard one: the max might be buried. So:
#     1. pop things into a temporary buffer until the max is on top
#     2. pop the max
#     3. push the buffer back (newest last)
#   That's O(n) for popMax. A fully O(log n) popMax needs a balanced tree
#   + linked list (or a heap with lazy deletion) - tools you'll build later.
# ============================================================


class MaxStackBrute:
    # Single list; peekMax and popMax scan the list.
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        biggest = self.stack[0]
        for v in self.stack:
            if v > biggest:
                biggest = v
        return biggest

    def popMax(self):
        biggest = self.peekMax()
        for i in range(len(self.stack) - 1, -1, -1):   # closest to the top
            if self.stack[i] == biggest:
                return self.stack.pop(i)


class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxes = []                 # maxes[i] = max of stack[0..i]

    def push(self, x):
        if len(self.maxes) == 0 or x > self.maxes[-1]:
            self.maxes.append(x)
        else:
            self.maxes.append(self.maxes[-1])
        self.stack.append(x)

    def pop(self):
        self.maxes.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.maxes[-1]

    def popMax(self):
        target = self.maxes[-1]
        buffer = []
        while self.stack[-1] != target:
            buffer.append(self.pop())   # dig down to the max
        self.pop()                      # remove the max itself
        while len(buffer) > 0:
            self.push(buffer.pop())     # put everything back (keeps maxes correct)
        return target


if __name__ == "__main__":
    ms = MaxStack()
    ms.push(5); ms.push(1); ms.push(5)
    print(ms.top())       # 5
    print(ms.popMax())    # 5
    print(ms.top())       # 1
    print(ms.peekMax())   # 5
    print(ms.pop())       # 1
    print(ms.top())       # 5
