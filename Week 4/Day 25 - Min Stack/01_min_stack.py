# ============================================================
# Day 25 - PRIMARY: Min Stack  (LeetCode 155)
# ============================================================
# The question:
#   Design a stack with four operations, ALL in O(1) time:
#     push(val), pop(), top(), getMin()  <- smallest value currently in the stack
#
#   Example: push(-2), push(0), push(-3)
#            getMin() -> -3
#            pop()
#            top()    -> 0
#            getMin() -> -2
#
# The big idea (carry extra state alongside the main stack):
#   The tricky part is getMin after a pop: if we popped the minimum, what
#   was the minimum BEFORE it arrived?
#   Answer: keep a second stack, 'mins', that remembers it.
#     push(val): also push val onto mins if val <= mins[-1]
#                (<= matters: duplicates of the min must be tracked too)
#     pop():     if the popped value == mins[-1], pop mins too
#     getMin():  mins[-1]
#   Two lists, every op O(1). (No heapq - a heap makes getMin O(log n)
#   and misses the whole lesson.)
# ============================================================


class MinStackBrute:
    # Brute force: a single list; getMin scans everything. O(n) getMin.
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        smallest = self.stack[0]
        for x in self.stack:
            if x < smallest:
                smallest = x
        return smallest


class MinStack:
    def __init__(self):
        self.stack = []             # the real values
        self.mins = []              # mins[-1] is always the current minimum

    def push(self, val):
        self.stack.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)   # a new (or tied) minimum

    def pop(self):
        val = self.stack.pop()
        if val == self.mins[-1]:
            self.mins.pop()         # the minimum is leaving; the old one is underneath

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())   # -3
    ms.pop()
    print(ms.top())      # 0
    print(ms.getMin())   # -2

    d = MinStack()       # duplicates of the minimum
    d.push(1); d.push(1); d.pop()
    print(d.getMin())    # 1
