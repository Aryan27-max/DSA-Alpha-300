# ============================================================
# Day 29 - PRIMARY: Best Time to Buy and Sell Stock  (LeetCode 121)
# ============================================================
# The question:
#   prices[i] is a stock's price on day i. Buy on one day and sell on a
#   LATER day. Return the biggest profit possible, or 0 if you can't make
#   any.
#
#   Example: [7,1,5,3,6,4] -> 5   (buy at 1, sell at 6)
#            [7,6,4,3,1]   -> 0   (prices only fall)
#
# The big idea (single-pass tracking):
#   If you sell today, the best day to have bought is the CHEAPEST day
#   so far. So walk once and keep two variables:
#     running_min  = cheapest price seen so far
#     best_profit  = best "today - running_min" seen so far
#   That "keep the best choice so far and decide on the spot" is your
#   first taste of greedy thinking (December).
#   (No min() / max() calls inside the loop - two plain if-checks.)
# ============================================================


def max_profit_brute(prices):
    # Brute force: try every buy day with every later sell day.
    best = 0
    n = len(prices)
    for buy in range(n):
        for sell in range(buy + 1, n):
            profit = prices[sell] - prices[buy]
            if profit > best:
                best = profit
    return best


def max_profit(prices):
    running_min = prices[0]
    best_profit = 0

    for price in prices:
        if price < running_min:
            running_min = price                 # a cheaper day to buy
        elif price - running_min > best_profit:
            best_profit = price - running_min   # selling today beats our record

    return best_profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))         # 5
    print(max_profit([7, 6, 4, 3, 1]))            # 0
    print(max_profit([2, 4, 1]))                  # 2
    print(max_profit_brute([7, 1, 5, 3, 6, 4]))   # 5
