# ============================================================
# Day 27 - VARIANT: Implement Stack using Queues  (LeetCode 225)
# ============================================================
# The question:
#   The reverse direction: build a LIFO stack (push, pop, top, empty)
#   using ONLY queue operations: push to back, pop from front, peek
#   front, size, is empty.
#
#   Example: push(1), push(2), top() -> 2, pop() -> 2, empty() -> False
#
# First we need a queue that obeys those rules. No deque - we build one:
#   a list + a 'head' pointer. pop_front just moves head forward.
#
# The big idea (one queue, rotate after every push):
#   After pushing x to the back, rotate: pop from the front and push to
#   the back (size - 1) times. Now x is at the FRONT, so the front of the
#   queue is always the "top" of the stack.
#   push is O(n), pop/top are O(1).
#
# Brute force (two queues): push is O(1), but pop moves n-1 elements into
# the second queue to reach the last one -> O(n) pop.
# ============================================================


class SimpleQueue:
    # A queue made from a list + head pointer. Only queue operations allowed.
    def __init__(self):
        self.items = []
        self.head = 0

    def push_back(self, x):
        self.items.append(x)

    def pop_front(self):
        x = self.items[self.head]
        self.head += 1
        if self.head > 32 and self.head * 2 > len(self.items):
            self.items = self.items[self.head:]   # occasionally drop the dead space
            self.head = 0
        return x

    def front(self):
        return self.items[self.head]

    def size(self):
        return len(self.items) - self.head


class MyStackBrute:
    # Two queues; pop moves everything except the last element across.
    def __init__(self):
        self.q1 = SimpleQueue()
        self.q2 = SimpleQueue()

    def push(self, x):
        self.q1.push_back(x)

    def pop(self):
        while self.q1.size() > 1:
            self.q2.push_back(self.q1.pop_front())
        top = self.q1.pop_front()
        self.q1, self.q2 = self.q2, self.q1     # swap roles
        return top

    def top(self):
        x = self.pop()
        self.push(x)                            # put it back
        return x

    def empty(self):
        return self.q1.size() == 0


class MyStack:
    def __init__(self):
        self.q = SimpleQueue()

    def push(self, x):
        self.q.push_back(x)
        for _ in range(self.q.size() - 1):
            self.q.push_back(self.q.pop_front())   # rotate x to the front

    def pop(self):
        return self.q.pop_front()

    def top(self):
        return self.q.front()

    def empty(self):
        return self.q.size() == 0


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.top())     # 2
    print(s.pop())     # 2
    print(s.empty())   # False
    print(s.pop())     # 1
    print(s.empty())   # True
