# Day 4 · Running Sum of 1d Array
**Topic:** Prefix sum intro

A prefix sum just means "keep a running total as you walk." It turns "add up a range" from a loop into a single subtraction. Today's problems are gentle on purpose — the goal is to make the carry-the-total habit automatic before Week 3's prefix-sum cluster.

> No `itertools.accumulate()`. Write the loop.

---

## 1. Running Sum of 1d Array (PRIMARY) — `01_running_sum.py`
Each position holds the sum of everything up to and including it.

**Brute force:** For every `i`, add up `nums[0..i]` again from scratch.
Time **O(n²)** · Space **O(n)** for the output

**Optimal:** Carry one `total` forward and append it each step (or update the list in place).
Time **O(n)** · Space **O(1)** extra (in-place version)

**Equivalent questions:** LeetCode 1480 – [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) · GFG – "Prefix Sum Array"

---

## 2. Range Sum Query – Immutable — `02_range_sum_query_immutable.py`
Answer lots of "sum from left to right" questions on a list that never changes.

**Brute force:** Loop over the range on every query.
Time **O(n) per query** · Space **O(1)**

**Optimal:** Build `prefix` once (with a 0 at the front). Answer = `prefix[right+1] - prefix[left]`.
Time **O(n) build, O(1) per query** · Space **O(n)**

**Equivalent questions:** LeetCode 303 – [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) · GFG – "Range sum queries"

---

## 3. Build Array from Permutation — `03_build_array_from_permutation.py`
`ans[i] = nums[nums[i]]`.

**Brute force / simple:** Build a new list.
Time **O(n)** · Space **O(n)**

**Optimal (follow-up):** Store old and new in the same slot: `nums[i] += n * (nums[nums[i]] % n)`, then divide everything by `n`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1920 – [Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/) · GFG – "Rearrange an array so that arr[i] becomes arr[arr[i]]"

---

## 4. Shuffle the Array — `04_shuffle_the_array.py`
`[x1..xn, y1..yn]` → `[x1, y1, x2, y2, ...]`.

**Brute force:** Copy into two separate halves, then interleave.
Time **O(n)** · Space **O(n)** extra

**Optimal:** One loop, append `nums[i]` then `nums[i+n]`.
Time **O(n)** · Space **O(n)** for the output only

**Equivalent questions:** LeetCode 1470 – [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/)

---

## 5. Richest Customer Wealth — `05_richest_customer_wealth.py`
Biggest row sum in a 2D grid.

**Brute force:** Store every row total in a list, then scan it for the max.
Time **O(m·n)** · Space **O(m)**

**Optimal:** Sum each row and compare on the spot. No extra list.
Time **O(m·n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1672 – [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) · GFG – "Row with max sum"

---

## 6. Left and Right Sum Differences — `06_left_right_sum_differences.py`
`|sum before i − sum after i|` for every `i`.

**Brute force:** For every `i`, add up the left side and the right side separately.
Time **O(n²)** · Space **O(1)** extra

**Optimal:** Find `total` once. Walk with `left_sum`; `right_sum = total − left_sum − nums[i]`.
Time **O(n)** · Space **O(1)** extra

**Equivalent questions:** LeetCode 2574 – [Left and Right Sum Differences](https://leetcode.com/problems/left-and-right-sum-differences/) · LeetCode 724 – [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) (same left/right idea) · GFG – "Equilibrium Point"
