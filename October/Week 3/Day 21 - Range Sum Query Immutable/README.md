# Day 21 · Range Sum Query – Immutable
**Topic:** Prefix sum — static range queries

**Build once, query many.** Spend O(n) up front building a prefix array, and every "sum from l to r" becomes one subtraction. The variants stretch the idea: to 2D grids, to "how many subarrays hit k" (prefix + hashmap = Two Sum again), to remainders, to products, and finally to a Fenwick tree when the array can change.

> No `itertools.accumulate()`. Build every prefix array with a loop.

---

## 1. Range Sum Query – Immutable (PRIMARY) — `01_range_sum_query_immutable.py`

**Brute force:** Loop over the range on every query.
Time **O(n) per query** · Space **O(1)**

**Optimal:** `prefix[i+1] = prefix[i] + nums[i]` in `__init__`; `sumRange = prefix[r+1] − prefix[l]`.
Time **O(n) build, O(1) per query** · Space **O(n)**

**Equivalent questions:** LeetCode 303 – [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) · GFG – "Prefix Sum Array"

---

## 2. Range Sum Query 2D – Immutable — `02_range_sum_query_2d.py`

**Brute force:** Loop over every cell in the rectangle.
Time **O(rows · cols) per query** · Space **O(1)**

**Optimal:** 2D prefix sums with inclusion–exclusion (add top and left, subtract the double-counted corner).
Time **O(R·C) build, O(1) per query** · Space **O(R·C)**

**Equivalent questions:** LeetCode 304 – [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) · LeetCode 1314 – [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) · GFG – "Sum of submatrix"

---

## 3. Subarray Sum Equals K — `03_subarray_sum_equals_k.py`

**Brute force:** Every start, extend and count sums equal to k.
Time **O(n²)** · Space **O(1)**

**Optimal:** Walk with a running prefix; count earlier prefixes equal to `prefix − k` using a dict seeded with `{0: 1}`. (Two Sum on prefix sums.)
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 560 – [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) · GFG – "Subarrays with sum K" · LeetCode 930 – [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)

---

## 4. Continuous Subarray Sum — `04_continuous_subarray_sum.py`

**Brute force:** Every subarray of length ≥ 2.
Time **O(n²)** · Space **O(1)**

**Optimal:** Same remainder (`prefix % k`) seen twice → the part between is a multiple of k. Store the **first** index for each remainder (seed `{0: -1}`) and check the gap ≥ 2.
Time **O(n)** · Space **O(min(n, k))**

**Equivalent questions:** LeetCode 523 – [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) · LeetCode 974 – [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

---

## 5. Product of Array Except Self — `05_product_except_self.py`

**Brute force:** For each index, multiply all the others.
Time **O(n²)** · Space **O(1)** extra

**Optimal:** Left pass writes the prefix product into `answer`; right pass multiplies in a running suffix product. No division.
Time **O(n)** · Space **O(1)** extra (output not counted)

**Equivalent questions:** LeetCode 238 – [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) · GFG – "Product array puzzle"

---

## 6. Range Sum Query – Mutable — `06_range_sum_query_mutable.py`

**Brute force:** Plain list — update O(1), query O(n). (A plain prefix array flips it: query O(1), update O(n).)

**Optimal:** Fenwick tree (Binary Indexed Tree), built by hand. `update` and `prefix_sum` both jump by the lowest set bit `i & -i`.
Time **O(n log n) build, O(log n) update, O(log n) query** · Space **O(n)**

**Equivalent questions:** LeetCode 307 – [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) · GFG – "Binary Indexed Tree or Fenwick Tree" · GFG – "Segment Tree | Sum of given range"
