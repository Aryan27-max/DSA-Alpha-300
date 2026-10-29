# Week 5 · October DSA (Oct 29 – Oct 31)
**Theme:** Consolidation — cross-pattern review before November (recursion + linked lists + binary search + sorting)

| Day | Primary problem | Topic |
|---|---|---|
| 29 | Best Time to Buy and Sell Stock | Single-pass tracking (arrays revisit) |
| 30 | Move Zeroes | Two pointers revisit (read + write) |
| 31 | Backspace String Compare | Stacks revisit (two stacks compared) |

Each day folder has one `.py` file per problem (`01_` is always the primary, the rest are variants) and a `README.md` with brute force, optimal approach, complexity and the matching LeetCode / GFG questions.

**Run any file:** `python3 "Day 29 - Best Time to Buy and Sell Stock/01_best_time_to_buy_sell_stock.py"`

**Rules this week:**
- Day 29: no `min()` / `max()` inside the loop — `if` checks or a hand-written `bigger(a, b)`.
- Day 30: no `sort(key=...)`, `filter()`, or list comprehensions + padding — in place, O(1) extra space.
- Day 31: no `deque`; bonus O(1)-space version with two reverse pointers.
- Still no imports anywhere.

**Repeats solved from a new angle:**
- Remove Element (swap-with-end), Remove Duplicates (general "keep at most k" template), Sort Array By Parity (pointers from both ends) — Day 10 used read/write for all three.
- Remove Adjacent Duplicates: Day 23 separate stack → Day 31 stack inside the array.
- Reverse Only Letters: Day 8/18 two pointers → Day 31 stack version beside it.

**Looking ahead to November:** Sort Array By Parity's both-ends loop is quicksort's partition; Rotate Array and Next Greater Element III reuse the reverse helper; the stock-state variables are your first DP.
