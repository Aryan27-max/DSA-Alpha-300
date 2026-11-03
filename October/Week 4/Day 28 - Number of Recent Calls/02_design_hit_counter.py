# ============================================================
# Day 28 - VARIANT: Design Hit Counter  (LeetCode 362 - Premium)
# ============================================================
# The question:
#   HitCounter:
#     hit(timestamp)      - a hit happened at this second
#     getHits(timestamp)  - how many hits in the last 300 seconds,
#                           i.e. in (timestamp - 300, timestamp]
#   Timestamps never go backwards, and many hits can share a timestamp.
#
#   Example: hit(1), hit(2), hit(3), getHits(4) -> 3,
#            hit(300), getHits(300) -> 4, getHits(301) -> 3
#
# The big idea (time-window counter):
#   Version A - queue of timestamps (list + head). getHits drops old ones
#     from the front. Memory grows with the number of hits in the window.
#   Version B - 300 buckets in a ring, one per second (timestamp % 300).
#     Each bucket stores (which second it belongs to, how many hits).
#     If a bucket holds an old second, reset it before reusing it.
#     getHits adds up the buckets that are still inside the window.
#     Memory is ALWAYS 300 slots, no matter how many hits come in.
# ============================================================


class HitCounterBrute:
    # Brute force: store every hit forever, count the window from scratch.
    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        count = 0
        for t in self.hits:
            if timestamp - t < 300:
                count += 1
        return count


class HitCounterQueue:
    def __init__(self):
        self.q = []
        self.head = 0

    def hit(self, timestamp):
        self.q.append(timestamp)

    def getHits(self, timestamp):
        while self.head < len(self.q) and self.q[self.head] <= timestamp - 300:
            self.head += 1              # too old - drop from the front
        return len(self.q) - self.head


class HitCounter:
    def __init__(self):
        self.times = [0] * 300          # which second each bucket currently holds
        self.counts = [0] * 300         # how many hits in that second

    def hit(self, timestamp):
        i = timestamp % 300
        if self.times[i] != timestamp:
            self.times[i] = timestamp   # bucket held an old second - reset it
            self.counts[i] = 1
        else:
            self.counts[i] += 1

    def getHits(self, timestamp):
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.counts[i]
        return total


if __name__ == "__main__":
    for cls in (HitCounterQueue, HitCounter):
        hc = cls()
        hc.hit(1); hc.hit(2); hc.hit(3)
        a = hc.getHits(4)
        hc.hit(300)
        b = hc.getHits(300)
        c = hc.getHits(301)
        print(cls.__name__, a, b, c)    # 3 4 3
