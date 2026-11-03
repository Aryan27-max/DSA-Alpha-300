# ============================================================
# Day 27 - PRIMARY: Implement Queue using Stacks  (LeetCode 232)
# ============================================================
# The question:
#   Build a FIFO queue (first in, first out) with push, pop, peek, empty,
#   using ONLY stack operations: push to top, pop from top, peek top,
#   size, is empty.
#
#   Example: push(1), push(2), peek() -> 1, pop() -> 1, empty() -> False
#
# The big idea (two stacks = one queue):
#   A stack reverses order. Reverse twice and you're back to the
#   original order - that's FIFO.
#     in_stack:  every push lands here.
#     out_stack: pops/peeks are served from here.
#   When out_stack is empty and someone wants the front, pour EVERYTHING
#   from in_stack into out_stack. The oldest element ends up on top.
#   Only pour when out_stack is empty - otherwise you'd bury the front.
#
# Why is that O(1)? (amortized analysis)
#   One pour can move n elements, so a single pop can cost O(n).
#   But each element is moved from in_stack to out_stack AT MOST ONCE in
#   its whole life: pushed once, moved once, popped once = 3 steps.
#   n operations cost at most 3n steps in total -> O(1) per op on average.
#   (No deque - that's already a queue and would skip the whole exercise.)
# ============================================================


class MyQueueBrute:
    # Brute force: keep the oldest element on TOP of a single stack by
    # rebuilding the stack on every push. Push O(n), pop O(1).
    def __init__(self):
        self.stack = []

    def push(self, x):
        temp = []
        while len(self.stack) > 0:
            temp.append(self.stack.pop())   # move everything out
        self.stack.append(x)                # newest goes to the bottom
        while len(temp) > 0:
            self.stack.append(temp.pop())   # move everything back on top

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def _pour_if_needed(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())  # reverses the order

    def pop(self):
        self._pour_if_needed()
        return self.out_stack.pop()

    def peek(self):
        self._pour_if_needed()
        return self.out_stack[-1]

    def empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())    # 1
    print(q.pop())     # 1
    q.push(3)
    print(q.pop())     # 2
    print(q.pop())     # 3
    print(q.empty())   # True
