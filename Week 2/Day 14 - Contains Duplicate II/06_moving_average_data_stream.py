# ============================================================
# Day 14 - VARIANT: Moving Average from Data Stream  (LeetCode 346 - Premium)
# ============================================================
# The question:
#   Build a class MovingAverage(size). Each call next(val) adds a number
#   from a stream and returns the average of the LAST size numbers
#   (or of all numbers so far, if fewer than size have arrived).
#
#   Example: m = MovingAverage(3)
#            m.next(1) -> 1.0
#            m.next(10) -> 5.5
#            m.next(3) -> 4.666...
#            m.next(5) -> 6.0   (average of 10, 3, 5)
#
# The big idea (sliding window over a stream):
#   Keep a running sum and a queue of the window's values.
#   New value in -> add to sum. If the window is too big, pop the oldest
#   and subtract it. Each call is O(1).
#   No collections.deque! Two hand-made options:
#     - a list + a 'head' pointer (we never actually delete from the front)
#     - a fixed-size circular buffer (used below - O(size) memory forever)
# ============================================================


class MovingAverageBrute:
    # Brute force: store everything, re-add the last `size` values each time.
    def __init__(self, size):
        self.size = size
        self.values = []

    def next(self, val):
        self.values.append(val)
        start = max(0, len(self.values) - self.size)
        total = 0
        for i in range(start, len(self.values)):
            total += self.values[i]
        return total / (len(self.values) - start)


class MovingAverageListQueue:
    # Queue made from a list + head pointer (the list keeps growing).
    def __init__(self, size):
        self.size = size
        self.items = []
        self.head = 0                   # index of the oldest value still in the window
        self.total = 0

    def next(self, val):
        self.items.append(val)
        self.total += val
        if len(self.items) - self.head > self.size:
            self.total -= self.items[self.head]     # oldest value slides out
            self.head += 1
        return self.total / (len(self.items) - self.head)


class MovingAverage:
    # Circular buffer: a fixed list of `size` slots that we overwrite in a loop.
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
        self.count = 0                  # how many values we've received in total
        self.total = 0

    def next(self, val):
        slot = self.count % self.size   # where this value goes (wraps around)
        if self.count >= self.size:
            self.total -= self.buffer[slot]     # remove the value we're overwriting
        self.buffer[slot] = val
        self.total += val
        self.count += 1
        return self.total / min(self.count, self.size)


if __name__ == "__main__":
    m = MovingAverage(3)
    print(m.next(1))     # 1.0
    print(m.next(10))    # 5.5
    print(m.next(3))     # 4.666666666666667
    print(m.next(5))     # 6.0

    q = MovingAverageListQueue(3)
    print([q.next(v) for v in [1, 10, 3, 5]])   # same four answers
