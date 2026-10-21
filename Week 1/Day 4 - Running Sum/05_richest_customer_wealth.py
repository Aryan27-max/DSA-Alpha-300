# ============================================================
# Day 4 - VARIANT: Richest Customer Wealth  (LeetCode 1672)
# ============================================================
# The question:
#   accounts[i][j] = money customer i has in bank j.
#   A customer's wealth = total of their row. Return the biggest wealth.
#
#   Example: [[1, 2, 3], [3, 2, 1]] -> 6
#
# The big idea:
#   Add up each row (accumulate), compare it to the best so far.
#   Nothing fancy - just don't build a whole list of sums if you don't need it.
# ============================================================


def maximum_wealth_brute(accounts):
    # Build a list of every customer's total, then find the max by hand.
    totals = []
    for customer in accounts:
        s = 0
        for money in customer:
            s += money
        totals.append(s)
    best = totals[0]
    for t in totals:
        if t > best:
            best = t
    return best


def maximum_wealth(accounts):
    best = 0
    for customer in accounts:
        wealth = 0
        for money in customer:
            wealth += money             # this customer's total
        if wealth > best:
            best = wealth               # new richest customer
    return best


if __name__ == "__main__":
    print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))            # 6
    print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))          # 10
    print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])) # 17
