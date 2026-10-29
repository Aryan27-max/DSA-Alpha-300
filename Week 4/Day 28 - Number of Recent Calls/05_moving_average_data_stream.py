# ============================================================
# Day 28 - VARIANT: Moving Average from Data Stream  (LeetCode 346 - Premium)
# ============================================================
# The question:
#   MovingAverage(size). next(val) returns the average of the last `size`
#   values seen (or all of them, if fewer have arrived).
#
#   Example: size 3: 1 -> 1.0, 10 -> 5.5, 3 -> 4.666..., 5 -> 6.0
#
# Today's angle - pop(0) vs a ring buffer (the comparison the plan asks for):
#   Day 14 used a circular buffer, Day 27 used the two-stack queue.
#   Here are both "first try" and "final" versions side by side:
#   - MovingAveragePop0: list + pop(0). Looks O(1), but pop(0) shifts
#     every element left -> O(size) per call.
#   - MovingAverage: fixed ring of `size` slots. The slot we overwrite IS
#     the value leaving the window. Truly O(1), memory never grows.
# ============================================================


class MovingAveragePop0:
    def __init__(self, size):
        self.size = size
        self.window = []
        self.total = 0

    def next(self, val):
        self.window.append(val)
        self.total += val
        if len(self.window) > self.size:
            self.total -= self.window.pop(0)    # O(size) shift hiding in here
        return self.total / len(self.window)


class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.ring = [0] * size
        self.seen = 0                           # total values received
        self.total = 0

    def next(self, val):
        slot = self.seen % self.size
        if self.seen >= self.size:
            self.total -= self.ring[slot]       # the value being overwritten leaves
        self.ring[slot] = val
        self.total += val
        self.seen += 1
        count = self.seen if self.seen < self.size else self.size
        return self.total / count


if __name__ == "__main__":
    for cls in (MovingAveragePop0, MovingAverage):
        m = cls(3)
        print(cls.__name__, [m.next(v) for v in [1, 10, 3, 5]])
        # [1.0, 5.5, 4.666666666666667, 6.0]
