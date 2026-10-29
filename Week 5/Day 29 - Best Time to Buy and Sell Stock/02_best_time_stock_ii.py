# ============================================================
# Day 29 - VARIANT: Best Time to Buy and Sell Stock II  (LeetCode 122)
# ============================================================
# The question:
#   Same prices, but now you can make AS MANY transactions as you like
#   (you can hold at most one share at a time; you may buy and sell on
#   the same day). Return the max total profit.
#
#   Example: [7,1,5,3,6,4] -> 7   (buy 1 sell 5 = 4, buy 3 sell 6 = 3)
#            [1,2,3,4,5]   -> 4
#
# The big idea (multiple transactions = greedy):
#   Any rising stretch from a to b can be split into daily steps:
#     b - a = (day2 - day1) + (day3 - day2) + ...
#   So just collect every day-to-day INCREASE. Skip the decreases.
#   That's exactly as much as the best set of trades can make.
# ============================================================


def max_profit_brute(prices):
    # Brute force: try every choice (buy / sell / wait) on every day.
    # Exponential - only for small inputs.
    def go(day, holding):
        if day == len(prices):
            return 0
        best = go(day + 1, holding)                         # do nothing today
        if holding:
            sell = prices[day] + go(day + 1, False)
            if sell > best:
                best = sell
        else:
            buy = -prices[day] + go(day + 1, True)
            if buy > best:
                best = buy
        return best
    return go(0, False)


def max_profit(prices):
    total = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total += prices[i] - prices[i - 1]   # bank every upward step
    return total


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))         # 7
    print(max_profit([1, 2, 3, 4, 5]))            # 4
    print(max_profit([7, 6, 4, 3, 1]))            # 0
    print(max_profit_brute([7, 1, 5, 3, 6, 4]))   # 7
