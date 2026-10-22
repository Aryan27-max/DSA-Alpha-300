# Day 20 · Find Pivot Index
**Topic:** Prefix sum — split point

Can you cut the array where the left sum equals the right sum? With the **total** in hand, the right sum at any index is just `total − left − nums[i]`, so one running variable answers the question for every index. The variants ask the same thing under other names, or ask about the running sum's lowest dip.

> No `itertools.accumulate()` and no `sum(nums[:i])` inside the loop (that's O(n²)). Keep `total` + a running `left` in O(n).

---

## 1. Find Pivot Index (PRIMARY) — `01_find_pivot_index.py`

**Brute force:** For each index, add up both sides from scratch.
Time **O(n²)** · Space **O(1)**

**Optimal:** Compute `total`; walk with `left_sum`; `right_sum = total − left_sum − nums[i]`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 724 – [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) · GFG – "Equilibrium Point"

---

## 2. Find the Middle Index in Array — `02_find_middle_index.py`
Same problem as the primary under a different name.

**Brute force:** Both sides from scratch for each index.
Time **O(n²)** · Space **O(1)**

**Optimal:** Same trick, written as `2 · left + nums[i] == total`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1991 – [Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/) · LeetCode 724 (identical)

---

## 3. Equilibrium Point (GFG) — `03_equilibrium_point.py`
Same idea, answer is 1-based (older GFG version; newer one is 0-based — subtract 1).

**Prefix + suffix arrays:** Build both, find the first index where they match.
Time **O(n)** · Space **O(n)**

**Optimal:** Total + running left.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** GFG – "Equilibrium Point" · LeetCode 724 – [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

---

## 4. Minimum Value to Get Positive Step by Step Sum — `04_min_value_positive_step_sum.py`

**Brute force:** Try start values 1, 2, 3, … and simulate each.
Time **O(n · answer)** · Space **O(1)**

**Optimal:** Track the lowest prefix sum (starting from 0). Answer = `1 − lowest`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1413 – [Minimum Value to Get Positive Step by Step Sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/)

---

## 5. Left and Right Sum Differences — `05_left_right_sum_differences.py`

**Brute force / two arrays:** Build `leftSum[]` and `rightSum[]`, then take differences.
Time **O(n)** · Space **O(n)** extra

**Optimal:** Total + running left, compute `|left − right|` on the fly.
Time **O(n)** · Space **O(1)** extra

**Equivalent questions:** LeetCode 2574 – [Left and Right Sum Differences](https://leetcode.com/problems/left-and-right-sum-differences/)

---

## 6. Running Sum of 1d Array — `06_running_sum.py`

**Brute force:** Re-add from index 0 for every position.
Time **O(n²)** · Space **O(n)**

**Optimal:** In place, `nums[i] += nums[i−1]`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1480 – [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) · GFG – "Prefix Sum Array"
