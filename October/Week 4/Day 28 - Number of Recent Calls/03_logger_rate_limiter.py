# ============================================================
# Day 28 - VARIANT: Logger Rate Limiter  (LeetCode 359 - Premium)
# ============================================================
# The question:
#   shouldPrintMessage(timestamp, message) returns True if the message
#   should be printed. The same message may be printed at most once every
#   10 seconds: if printed at time t, it's blocked until t + 10.
#   Timestamps arrive in non-decreasing order.
#
#   Example: (1,"foo") True, (2,"bar") True, (3,"foo") False,
#            (8,"bar") False, (10,"foo") False, (11,"foo") True
#
# The big idea (rate limit per message):
#   Version A - dict: message -> the earliest time it may print again. O(1).
#     Downside: the dict remembers every message forever.
#   Version B - bounded memory with a queue: keep only messages printed in
#     the last 10 seconds (queue of (time, message) + a set of those
#     messages). Before answering, drop everything 10+ seconds old.
#     Memory now depends only on traffic in the last 10 seconds.
# ============================================================


class LoggerBrute:
    # Brute force: keep every printed (time, message); scan for a recent one.
    def __init__(self):
        self.printed = []

    def shouldPrintMessage(self, timestamp, message):
        for t, m in self.printed:
            if m == message and timestamp - t < 10:
                return False
        self.printed.append((timestamp, message))
        return True


class LoggerDict:
    def __init__(self):
        self.next_allowed = {}          # message -> earliest time it can print again

    def shouldPrintMessage(self, timestamp, message):
        if timestamp < self.next_allowed.get(message, 0):
            return False
        self.next_allowed[message] = timestamp + 10
        return True


class Logger:
    def __init__(self):
        self.q = []                     # (time, message) printed recently
        self.head = 0
        self.recent = set()             # messages currently in the queue

    def shouldPrintMessage(self, timestamp, message):
        while self.head < len(self.q) and timestamp - self.q[self.head][0] >= 10:
            self.recent.discard(self.q[self.head][1])   # 10+ seconds old - forget it
            self.head += 1
        if message in self.recent:
            return False
        self.q.append((timestamp, message))
        self.recent.add(message)
        return True


if __name__ == "__main__":
    calls = [(1, "foo"), (2, "bar"), (3, "foo"), (8, "bar"), (10, "foo"), (11, "foo")]
    for cls in (LoggerDict, Logger):
        lg = cls()
        print(cls.__name__, [lg.shouldPrintMessage(t, m) for t, m in calls])
        # [True, True, False, False, False, True]
