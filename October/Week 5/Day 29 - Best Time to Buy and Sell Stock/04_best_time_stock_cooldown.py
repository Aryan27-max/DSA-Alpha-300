# ============================================================
# Day 29 - VARIANT: Best Time to Buy and Sell Stock with Cooldown  (LeetCode 309)
# ============================================================
# The question:
#   Unlimited transactions, but after you SELL you must wait one day
#   (cooldown) before buying again. Max profit?
#
#   Example: [1,2,3,0,2] -> 3   (buy, sell, cooldown, buy, sell)
#
# The big idea (three states, carried day to day):
#   Each day you're in exactly one state:
#     hold = you own a share
#     sold = you sold TODAY (so tomorrow is a cooldown)
#     rest = you own nothing and are free to buy tomorrow
#   Tomorrow's values only depend on today's:
#     new_hold = bigger(hold, rest - price)    keep holding, or buy (only from rest)
#     new_sold = hold + price                  sell what you hold
#     new_rest = bigger(rest, sold)            stay out, or finish the cooldown
#   Answer = bigger(sold, rest) at the end (never end still holding).
#   This "small set of states updated each day" is dynamic programming -
#   you'll meet it properly later.
# ============================================================


def bigger(a, b):
    return a if a > b else b


def max_profit_brute(prices):
    # Brute force: recursion over every choice. Exponential.
    def go(day, holding):
        if day >= len(prices):
            return 0
        best = go(day + 1, holding)                         # wait
        if holding:
            best = bigger(best, prices[day] + go(day + 2, False))   # sell, skip a day
        else:
            best = bigger(best, -prices[day] + go(day + 1, True))   # buy
        return best
    return go(0, False)


def max_profit(prices):
    hold = -prices[0]
    sold = 0
    rest = 0

    for i in range(1, len(prices)):
        p = prices[i]
        new_hold = bigger(hold, rest - p)
        new_sold = hold + p
        new_rest = bigger(rest, sold)
        hold, sold, rest = new_hold, new_sold, new_rest   # all three move together

    return bigger(sold, rest)


if __name__ == "__main__":
    print(max_profit([1, 2, 3, 0, 2]))         # 3
    print(max_profit([1]))                     # 0
    print(max_profit_brute([1, 2, 3, 0, 2]))   # 3
