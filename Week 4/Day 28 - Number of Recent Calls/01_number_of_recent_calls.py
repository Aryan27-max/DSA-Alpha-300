# ============================================================
# Day 28 - PRIMARY: Number of Recent Calls  (LeetCode 933)
# ============================================================
# The question:
#   RecentCounter.ping(t) records a request at time t (milliseconds) and
#   returns how many requests happened in the last 3000 ms, i.e. in the
#   range [t - 3000, t]. Every t is strictly bigger than the one before.
#
#   Example: ping(1) -> 1, ping(100) -> 2, ping(3001) -> 3, ping(3002) -> 3
#            (at 3002 the window is [2, 3002], so the ping at time 1 drops out)
#
# The big idea (queue as a sliding window of TIME):
#   Times arrive in increasing order, so old pings always leave from the
#   FRONT and new ones join at the BACK - a queue.
#   On each ping: add t at the back, drop pings older than t - 3000 from
#   the front, return the size.
#
#   Three versions, from simplest to best (no deque, no bisect):
#   v1  list + pop(0)      easy to write, but pop(0) shifts every element: O(n)
#   v2  list + head index  "pop" by moving head forward: O(1), but memory grows
#   v3  circular buffer    fixed 3001 slots, reused forever: O(1) time AND bounded memory
#       (3001 is enough: times are distinct integers, so at most 3001 fit in
#        any 3001-ms window.)
#   This exact shape - a queue of timestamps - is a rate limiter.
# ============================================================


class RecentCounterPop0:
    # v1: the simple version the plan asks you to write first.
    def __init__(self):
        self.q = []

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.pop(0)               # O(n): every remaining element shifts left
        return len(self.q)


class RecentCounterHead:
    # v2: never shift - just move a head pointer past old pings.
    def __init__(self):
        self.q = []
        self.head = 0

    def ping(self, t):
        self.q.append(t)
        while self.q[self.head] < t - 3000:
            self.head += 1              # O(1) "pop"
        return len(self.q) - self.head


class RecentCounter:
    # v3: fixed-size ring buffer.
    CAP = 3001

    def __init__(self):
        self.buf = [0] * self.CAP
        self.head = 0                   # oldest ping still in the window
        self.count = 0

    def ping(self, t):
        self.buf[(self.head + self.count) % self.CAP] = t
        self.count += 1
        while self.buf[self.head] < t - 3000:
            self.head = (self.head + 1) % self.CAP
            self.count -= 1
        return self.count


if __name__ == "__main__":
    for cls in (RecentCounterPop0, RecentCounterHead, RecentCounter):
        rc = cls()
        print(cls.__name__, [rc.ping(t) for t in [1, 100, 3001, 3002]])   # [1, 2, 3, 3]
