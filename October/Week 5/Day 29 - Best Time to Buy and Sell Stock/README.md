# Day 29 · Best Time to Buy and Sell Stock
**Topic:** Single-pass tracking (arrays revisit)

Walk once and carry just a couple of "best so far" variables. For one trade, that's the cheapest price so far and the best profit so far. Add rules (more trades, a cooldown, a fee) and you carry a few more variables — one per **state** you could be in. That's the bridge from greedy (December) to dynamic programming.

> No `min()` / `max()` calls inside the loop — plain `if` checks or a tiny hand-written `bigger(a, b)` helper.

---

## 1. Best Time to Buy and Sell Stock (PRIMARY) — `01_best_time_to_buy_sell_stock.py`

**Brute force:** Every buy day × every later sell day.
Time **O(n²)** · Space **O(1)**

**Optimal:** `running_min` and `best_profit` in one pass.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 121 – [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · GFG – "Stock Buy and Sell – Max one Transaction Allowed"

---

## 2. Best Time to Buy and Sell Stock II — `02_best_time_stock_ii.py`

**Brute force:** Recursively try buy / sell / wait on every day.
Time **O(2ⁿ)** · Space **O(n)** recursion

**Optimal (greedy):** Add up every day-to-day increase.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 122 – [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) · GFG – "Stock Buy and Sell – Multiple Transaction Allowed"

---

## 3. Best Time to Buy and Sell Stock III — `03_best_time_stock_iii.py`

**Brute force:** Try every split day; best single trade on each side.
Time **O(n²)** · Space **O(1)**

**Optimal:** Four running states `buy1, sell1, buy2, sell2`, each built on the previous one.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 123 – [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) · LeetCode 188 – [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) (k trades) · GFG – "Maximum profit by buying and selling a share at most twice"

---

## 4. Best Time to Buy and Sell Stock with Cooldown — `04_best_time_stock_cooldown.py`

**Brute force:** Recursion; selling jumps two days ahead.
Time **O(2ⁿ)** · Space **O(n)**

**Optimal:** Three states `hold`, `sold`, `rest` updated together each day.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 309 – [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

---

## 5. Best Time to Buy and Sell Stock with Transaction Fee — `05_best_time_stock_fee.py`

**Brute force:** Recursion over every choice, subtracting the fee on each sale.
Time **O(2ⁿ)** · Space **O(n)**

**Optimal:** Two states `cash` and `hold`; pay the fee when selling.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 714 – [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

---

## 6. Maximum Subarray — `06_maximum_subarray.py`

**Brute force:** Every start, extend and track the best sum.
Time **O(n²)** · Space **O(1)**

**Optimal (Kadane):** `current` = best sum ending here (restart when it's negative), `best` = best overall.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 53 – [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · GFG – "Kadane's Algorithm" · LeetCode 152 – [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (harder cousin)
