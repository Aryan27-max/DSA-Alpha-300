# Day 12 · Squares of a Sorted Array
**Topic:** Two pointers from both ends (compare absolute values)

Sorted input with negatives: after squaring, the biggest value is at one of the **ends**, not the middle. Ask "where does the extreme value live?" and you can often skip sorting entirely. The variants practise the same instinct — two-pointer swaps, edge-finding sweeps, counting sort when values are small, and max-minus-min prefix sums.

> No `sorted(x*x for x in nums)`. The goal is O(n), not O(n log n). Brute forces that need sorting use our own merge / insertion sort.

---

## 1. Squares of a Sorted Array (PRIMARY) — `01_squares_of_sorted_array.py`

**Brute force:** Square everything, then sort (our own merge sort).
Time **O(n log n)** · Space **O(n)**

**Optimal:** Two pointers from the ends, compare `abs()`, write the bigger square into the result from the back.
Time **O(n)** · Space **O(n)** for the output

**Equivalent questions:** LeetCode 977 – [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) · GFG – "Sort array after converting elements to their squares"

---

## 2. Sort Array By Parity II — `02_sort_array_by_parity_ii.py`
Even values at even indexes, odd values at odd indexes.

**Brute force:** New list, drop evens into slots 0,2,4… and odds into 1,3,5….
Time **O(n)** · Space **O(n)**

**Optimal:** Even pointer and odd pointer hop by 2; when both find a misplaced number, swap them.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 922 – [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/) · GFG – "Even and odd elements at even and odd positions"

---

## 3. Shortest Unsorted Continuous Subarray — `03_shortest_unsorted_subarray.py`

**Brute force:** Sort a copy, find the first and last positions that differ.
Time **O(n log n)** · Space **O(n)**

**Optimal:** Sweep left→right with a running max (anything smaller is misplaced → right edge), sweep right→left with a running min (anything bigger is misplaced → left edge).
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 581 – [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) · GFG – "Length of the unsorted subarray"

---

## 4. Height Checker — `04_height_checker.py`

**Brute force:** Insertion-sort a copy, compare position by position.
Time **O(n²)** · Space **O(n)**

**Optimal:** Counting sort (heights are 1..100): count each height, then walk heights in order while comparing with the real line.
Time **O(n + 100)** · Space **O(100) = O(1)**

**Equivalent questions:** LeetCode 1051 – [Height Checker](https://leetcode.com/problems/height-checker/) · GFG – "Counting Sort"

---

## 5. Relative Sort Array — `05_relative_sort_array.py`

**Brute force:** For each value in arr2, scan arr1 to collect it; insertion-sort the leftovers.
Time **O(n·m + r²)** · Space **O(n)**

**Optimal:** Count arr1 in a dict, write values in arr2's order, then write leftovers by walking 0..1000.
Time **O(n + m + 1000)** · Space **O(n)**

**Equivalent questions:** LeetCode 1122 – [Relative Sort Array](https://leetcode.com/problems/relative-sort-array/) · GFG – "Sort an array according to the other"

---

## 6. Maximum Absolute Sum of Any Subarray — `06_max_absolute_sum_subarray.py`

**Brute force:** Try every subarray.
Time **O(n²)** · Space **O(1)**

**Optimal:** Subarray sum = difference of two prefix sums, so answer = (max prefix) − (min prefix), counting the empty prefix 0. (Kadane twice also works — included.)
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1749 – [Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) · LeetCode 53 – [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · GFG – "Kadane's Algorithm"
