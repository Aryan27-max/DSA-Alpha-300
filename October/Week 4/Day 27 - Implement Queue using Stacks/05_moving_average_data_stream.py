# ============================================================
# Day 27 - VARIANT: Moving Average from Data Stream  (LeetCode 346 - Premium)
# ============================================================
# The question:
#   MovingAverage(size). next(val) adds a number and returns the average
#   of the last `size` numbers (or all of them if fewer have arrived).
#
#   Example: size 3: next(1) -> 1.0, next(10) -> 5.5, next(3) -> 4.666...,
#            next(5) -> 6.0
#
# Today's angle - a rolling average via OUR two-stack queue:
#   (Day 14 used a circular buffer, Day 28 compares pop(0) vs a ring.)
#   A moving window is a queue: newest in at the back, oldest out at the
#   front. Today's primary IS a queue, so reuse it:
#     push the new value, add it to the running sum,
#     if the queue holds more than `size` values, pop the oldest and
#     subtract it.
#   Each call is amortized O(1).
# ============================================================


class TwoStackQueue:
    # Today's primary, trimmed down: push / pop / size.
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def size(self):
        return len(self.in_stack) + len(self.out_stack)


class MovingAverageBrute:
    # Brute force: keep everything, re-add the last `size` values every call.
    def __init__(self, size):
        self.size = size
        self.values = []

    def next(self, val):
        self.values.append(val)
        start = len(self.values) - self.size
        if start < 0:
            start = 0
        total = 0
        for i in range(start, len(self.values)):
            total += self.values[i]
        return total / (len(self.values) - start)


class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.window = TwoStackQueue()
        self.total = 0

    def next(self, val):
        self.window.push(val)
        self.total += val
        if self.window.size() > self.size:
            self.total -= self.window.pop()     # oldest value leaves
        return self.total / self.window.size()


if __name__ == "__main__":
    m = MovingAverage(3)
    print(m.next(1))    # 1.0
    print(m.next(10))   # 5.5
    print(m.next(3))    # 4.666666666666667
    print(m.next(5))    # 6.0
