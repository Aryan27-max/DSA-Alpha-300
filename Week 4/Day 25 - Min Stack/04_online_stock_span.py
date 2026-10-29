# ============================================================
# Day 25 - VARIANT: Online Stock Span  (LeetCode 901)
# ============================================================
# The question:
#   Prices arrive one per day. next(price) returns today's "span": the
#   number of consecutive days, ending today, with price <= today's price.
#
#   Example: 100, 80, 60, 70, 60, 75, 85
#            ->  1,  1,  1,  2,  1,  4,  6
#
# The big idea (monotonic stack that carries extra state):
#   Keep a stack of (price, span) pairs with prices going DOWN from bottom
#   to top. When a new price arrives, every pair on top with price <= it
#   is "swallowed": add its span to ours and pop it.
#   Whatever's left on top is the previous HIGHER price, so the span stops
#   there. Each pair is pushed once and popped once -> amortized O(1).
#   Like Min Stack, the stack stores extra info (the span) next to each value.
# ============================================================


class StockSpannerBrute:
    # Brute force: store every price, walk backwards each time.
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 0
        i = len(self.prices) - 1
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1
        return span


class StockSpanner:
    def __init__(self):
        self.stack = []                 # (price, span) with prices decreasing upward

    def next(self, price):
        span = 1                        # today counts
        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            span += self.stack.pop()[1] # swallow that whole stretch
        self.stack.append((price, span))
        return span


if __name__ == "__main__":
    s = StockSpanner()
    print([s.next(p) for p in [100, 80, 60, 70, 60, 75, 85]])   # [1, 1, 1, 2, 1, 4, 6]
