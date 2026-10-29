# ============================================================
# Day 23 - VARIANT: Final Prices With a Special Discount in a Shop  (LeetCode 1475)
# ============================================================
# The question:
#   prices[i] is the price of item i. When you buy item i you get a
#   discount equal to prices[j] for the FIRST j > i with prices[j] <= prices[i]
#   (no discount if there is no such j). Return the final prices.
#
#   Example: [8,4,6,2,3] -> [4,2,4,2,3]
#            item 0 (8): first later price <= 8 is 4 -> 8 - 4 = 4
#
# The big idea (monotonic stack intro):
#   Keep a stack of indexes of items still WAITING for their discount.
#   Their prices on the stack go up from bottom to top (increasing).
#   When a new price p arrives, every waiting item on top with price >= p
#   has just found its discount -> pop it and subtract p.
#   Then push the new item (it now waits too).
#   Each index is pushed once and popped once -> O(n).
#   This "pop while the new value beats the top" move is the whole
#   monotonic-stack pattern you'll use all of Day 26.
# ============================================================


def final_prices_brute(prices):
    # Brute force: for each item, scan forward for the first price <= it.
    n = len(prices)
    result = []
    for i in range(n):
        discount = 0
        for j in range(i + 1, n):
            if prices[j] <= prices[i]:
                discount = prices[j]
                break
        result.append(prices[i] - discount)
    return result


def final_prices(prices):
    result = prices[:]              # start with full prices
    stack = []                      # indexes still waiting for a discount

    for i in range(len(prices)):
        p = prices[i]
        while len(stack) > 0 and prices[stack[-1]] >= p:
            waiting = stack.pop()
            result[waiting] -= p    # p is the first price <= theirs
        stack.append(i)

    return result


if __name__ == "__main__":
    print(final_prices([8, 4, 6, 2, 3]))         # [4, 2, 4, 2, 3]
    print(final_prices([1, 2, 3, 4, 5]))         # [1, 2, 3, 4, 5]
    print(final_prices([10, 1, 1, 6]))           # [9, 0, 1, 6]
    print(final_prices_brute([8, 4, 6, 2, 3]))   # [4, 2, 4, 2, 3]
