# Day 26 · Next Greater Element I
**Topic:** Monotonic decreasing stack

Keep a stack of things **still waiting** for an answer. When a new value arrives, it answers everyone on top that it beats — pop them, record the answer, then push the newcomer. Because beaten values are gone, the stack is always sorted (monotonic). Each item is pushed and popped once, so it's O(n). This pattern is behind temperatures, stock spans, histograms and sliding-window maximums.

> No `deque` or `bisect`. A plain list is the monotonic stack: push conditionally, pop while top < current.

---

## 1. Next Greater Element I (PRIMARY) — `01_next_greater_element_i.py`

**Brute force:** For each `x`, find it in `nums2`, scan right for the first bigger value.
Time **O(m·n)** · Space **O(1)** extra

**Optimal:** One pass over `nums2` with a decreasing stack; pop and record `next_greater[top] = x` while `top < x`. Look up `nums1` in the dict.
Time **O(m + n)** · Space **O(n)**

**Equivalent questions:** LeetCode 496 – [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) · GFG – "Next Greater Element"

---

## 2. Next Greater Element II — `02_next_greater_element_ii.py`

**Brute force:** For each index, walk forward with `% n` wrap-around.
Time **O(n²)** · Space **O(1)** extra

**Optimal:** Loop `i` from 0 to `2n − 1` using `nums[i % n]`; stack of indexes; only push on the first pass.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 503 – [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) · GFG – "Next Greater Element in Circular Array"

---

## 3. Next Greater Element III — `03_next_greater_element_iii.py`

**Brute force:** Try every arrangement of the digits; keep the smallest one > n.
Time **O(d! · d)** · Space **O(d)**

**Optimal (next permutation):** From the right, find the first digit smaller than its neighbour; swap it with the smallest bigger digit to its right; reverse the tail. Check the 32-bit limit.
Time **O(d)** · Space **O(d)** (d = number of digits)

**Equivalent questions:** LeetCode 556 – [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) · LeetCode 31 – [Next Permutation](https://leetcode.com/problems/next-permutation/) · GFG – "Next Permutation"

---

## 4. Daily Temperatures — `04_daily_temperatures.py`

**Brute force:** For each day, scan forward for a warmer one.
Time **O(n²)** · Space **O(1)** extra

**Optimal:** Decreasing stack of indexes; when popped, the wait is `today − day`.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 739 – [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

---

## 5. Largest Rectangle in Histogram — `05_largest_rectangle_histogram.py`

**Brute force:** Every start, extend right while tracking the lowest bar.
Time **O(n²)** · Space **O(1)**

**Optimal:** **Increasing** stack of indexes. A shorter bar pops taller ones; each popped bar's width = `i − (new top) − 1`. A fake height-0 bar at the end flushes everything.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 84 – [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) · LeetCode 85 – [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) · GFG – "Maximum Rectangular Area in a Histogram"

---

## 6. Sliding Window Maximum — `06_sliding_window_maximum.py`
(Day 25: two max-stacks · **Day 26: monotonic deque** · Day 28: circular-buffer deque.)

**Brute force:** Scan each window.
Time **O(n·k)** · Space **O(1)** extra

**Optimal:** Monotonic deque (list + head pointer). Pop smaller values from the back, expired index from the front; the front is the max.
Time **O(n)** · Space **O(n)** here (the list keeps old entries; Day 28's ring keeps it at O(k))

**Equivalent questions:** LeetCode 239 – [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) · GFG – "Maximum of all subarrays of size k"
