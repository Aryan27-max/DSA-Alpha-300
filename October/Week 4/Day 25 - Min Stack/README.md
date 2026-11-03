# Day 25 · Min Stack
**Topic:** Augmented stack (keep a 2nd stack for min)

A stack can carry **extra information** next to each value: the minimum so far, the maximum so far, a pending increment, a span. Each push and pop keeps that extra info in sync, so questions about the whole stack get answered in O(1). This idea comes back in max-stacks, LRU caches and more — and today's last file combines it with "two stacks make a queue" (Day 27).

> No `heapq`. A heap makes `getMin` O(log n) and skips the whole lesson. Target: all four ops O(1) with two lists.

---

## 1. Min Stack (PRIMARY) — `01_min_stack.py`

**Brute force:** One list; `getMin` scans it.
Time **O(1)** push/pop/top, **O(n)** getMin · Space **O(n)**

**Optimal:** Second list `mins`. Push onto it when `val <= mins[-1]`; pop it when the popped value equals `mins[-1]`.
Time **O(1)** for all four ops · Space **O(n)**

**Equivalent questions:** LeetCode 155 – [Min Stack](https://leetcode.com/problems/min-stack/) · GFG – "Get minimum element from stack"

---

## 2. Max Stack — `02_max_stack.py`

**Brute force:** One list; `peekMax` and `popMax` scan it.
Time **O(n)** peekMax/popMax · Space **O(n)**

**Two stacks:** `maxes[i]` = max of `stack[0..i]` → push/pop/top/peekMax O(1). `popMax` digs the max out into a buffer and pushes the rest back — **O(n)**.
*(O(log n) popMax needs a balanced tree + linked list, or a heap with lazy deletion — later months.)*

**Equivalent questions:** LeetCode 716 – [Max Stack](https://leetcode.com/problems/max-stack/) (Premium) · LeetCode 155 – [Min Stack](https://leetcode.com/problems/min-stack/) (free, same core idea)

---

## 3. Design a Stack With Increment Operation — `03_custom_stack_increment.py`

**Brute force:** `increment` loops over the bottom k.
Time **O(k)** increment · Space **O(n)**

**Optimal:** Lazy `inc` list. `increment` marks one slot; `pop` returns `stack[i] + inc[i]` and passes `inc[i]` down to `inc[i−1]`.
Time **O(1)** for every op · Space **O(n)**

**Equivalent questions:** LeetCode 1381 – [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/)

---

## 4. Online Stock Span — `04_online_stock_span.py`

**Brute force:** Keep all prices; walk backwards every call.
Time **O(n)** per call · Space **O(n)**

**Optimal:** Stack of `(price, span)` with decreasing prices; swallow every pair with price ≤ today's and add its span.
Time **amortized O(1)** per call · Space **O(n)**

**Equivalent questions:** LeetCode 901 – [Online Stock Span](https://leetcode.com/problems/online-stock-span/) · GFG – "Stock span problem"

---

## 5. Validate Stack Sequences — `05_validate_stack_sequences.py`

**Brute force:** Recursively try every push/pop choice.
Time **exponential** · Space **O(n)**

**Optimal:** Replay — push in order, greedily pop while the top matches `popped[j]`. (Bonus: reuse `pushed` as the stack for O(1) extra space.)
Time **O(n)** · Space **O(n)** (or **O(1)** extra with the bonus)

**Equivalent questions:** LeetCode 946 – [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/) · GFG – "Check if a stack permutation is valid"

---

## 6. Sliding Window Maximum — `06_sliding_window_maximum.py`
(Three versions this week: Day 25 two max-stacks · Day 26 monotonic deque · Day 28 circular-buffer deque.)

**Brute force:** Scan each window.
Time **O(n·k)** · Space **O(1)** extra

**Today's version:** A queue made of two max-stacks (each entry carries the running max). Window max = bigger of the two tops.
Time **O(n)** amortized · Space **O(k)**

**Equivalent questions:** LeetCode 239 – [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) · GFG – "Maximum of all subarrays of size k"
