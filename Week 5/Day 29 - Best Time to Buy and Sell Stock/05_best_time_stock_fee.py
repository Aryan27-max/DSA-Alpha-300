# ============================================================
# Day 29 - VARIANT: Best Time to Buy and Sell Stock with Transaction Fee  (LeetCode 714)
# ============================================================
# The question:
#   Unlimited transactions, but every completed trade costs `fee`.
#   Max profit?
#
#   Example: prices = [1,3,2,8,4,9], fee = 2 -> 8
#            (buy 1 sell 8: 7 - 2 = 5, buy 4 sell 9: 5 - 2 = 3)
#
# The big idea (two states):
#   cash = best balance while holding nothing
#   hold = best balance while holding a share
#   Each day:
#     cash = bigger(cash, hold + price - fee)   sell today (pay the fee)
#     hold = bigger(hold, cash - price)         buy today
#   The fee is why Stock II's "grab every small rise" no longer works:
#   lots of tiny trades each pay the fee.
# ============================================================


def bigger(a, b):
    return a if a > b else b


def max_profit_brute(prices, fee):
    def go(day, holding):
        if day == len(prices):
            return 0
        best = go(day + 1, holding)
        if holding:
            best = bigger(best, prices[day] - fee + go(day + 1, False))
        else:
            best = bigger(best, -prices[day] + go(day + 1, True))
        return best
    return go(0, False)


def max_profit(prices, fee):
    cash = 0
    hold = -prices[0]

    for i in range(1, len(prices)):
        p = prices[i]
        cash = bigger(cash, hold + p - fee)   # sell
        hold = bigger(hold, cash - p)         # buy (using today's cash is fine: same-day
                                              # sell+buy just wastes a fee, never helps)
    return cash


if __name__ == "__main__":
    print(max_profit([1, 3, 2, 8, 4, 9], 2))         # 8
    print(max_profit([1, 3, 7, 5, 10, 3], 3))        # 6
    print(max_profit_brute([1, 3, 2, 8, 4, 9], 2))   # 8
