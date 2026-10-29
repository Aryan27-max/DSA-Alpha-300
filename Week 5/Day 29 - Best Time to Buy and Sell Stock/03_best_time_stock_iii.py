# ============================================================
# Day 29 - VARIANT: Best Time to Buy and Sell Stock III  (LeetCode 123 - Hard)
# ============================================================
# The question:
#   At most TWO transactions (never hold two shares at once). Max profit?
#
#   Example: [3,3,5,0,0,3,1,4] -> 6   (buy 0 sell 3, buy 1 sell 4)
#            [1,2,3,4,5] -> 4         (one trade is enough)
#
# The big idea (four running variables - the primary, twice):
#   The primary tracked "cheapest buy so far" and "best profit so far".
#   Now track four "best balance so far" values, one per step:
#     buy1  = best balance after the 1st buy    (= -cheapest price)
#     sell1 = best balance after the 1st sell   (= one-trade answer)
#     buy2  = best balance after the 2nd buy    (sell1 - price)
#     sell2 = best balance after the 2nd sell   (the answer)
#   Update all four every day. Each one only builds on the one before it.
#   We use a small hand-written helper instead of max().
# ============================================================


def bigger(a, b):
    return a if a > b else b


def max_profit_brute(prices):
    # Brute force: split the days into a left part and a right part,
    # take the best single trade on each side, try every split. O(n^2).
    def one_trade(start, end):
        best = 0
        low = None
        for i in range(start, end):
            if low is None or prices[i] < low:
                low = prices[i]
            elif prices[i] - low > best:
                best = prices[i] - low
        return best

    best = 0
    n = len(prices)
    for split in range(n + 1):
        total = one_trade(0, split) + one_trade(split, n)
        if total > best:
            best = total
    return best


def max_profit(prices):
    buy1 = -prices[0]
    sell1 = 0
    buy2 = -prices[0]
    sell2 = 0

    for p in prices:
        buy1 = bigger(buy1, -p)             # cheapest first buy
        sell1 = bigger(sell1, buy1 + p)     # best first sale
        buy2 = bigger(buy2, sell1 - p)      # reinvest the first profit
        sell2 = bigger(sell2, buy2 + p)     # best second sale

    return sell2


if __name__ == "__main__":
    print(max_profit([3, 3, 5, 0, 0, 3, 1, 4]))         # 6
    print(max_profit([1, 2, 3, 4, 5]))                  # 4
    print(max_profit([7, 6, 4, 3, 1]))                  # 0
    print(max_profit_brute([3, 3, 5, 0, 0, 3, 1, 4]))   # 6
