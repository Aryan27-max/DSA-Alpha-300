# Day 3 · Single Number
**Topic:** XOR / bit trick

XOR is like a hashmap that costs zero memory: `a ^ a = 0` and `a ^ 0 = a`. XOR a bunch of numbers together and every pair disappears. Today is about spotting when that trick works — and what to do when it doesn't (three copies, two singles, sorted input).

> Using a hashmap on the primary means you skipped the lesson. The dict versions below are only there as the "brute force" to compare against.

---

## 1. Single Number (PRIMARY) — `01_single_number.py`
Everything appears twice except one.

**Brute force:** For every number, count its copies with an inner loop.
Time **O(n²)** · Space **O(1)**
(Or a dict: O(n) time, O(n) space.)

**Optimal:** XOR all numbers. Pairs cancel, the single one is left.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 136 – [Single Number](https://leetcode.com/problems/single-number/) · GFG – "Find the element that appears once"

---

## 2. Single Number II — `02_single_number_ii.py`
Everything appears three times except one.

**Brute force:** Count each number in a dict.
Time **O(n)** · Space **O(n)**

**Optimal:** For each of the 32 bits, add up that bit across all numbers and take `% 3`. That gives the bit of the single number. Fix the sign at the end.
Time **O(32·n) = O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 137 – [Single Number II](https://leetcode.com/problems/single-number-ii/) · GFG – "Find the element that appears once (others three times)"

---

## 3. Single Number III — `03_single_number_iii.py`
Everything appears twice except two numbers.

**Brute force:** Dict counting.
Time **O(n)** · Space **O(n)**

**Optimal:** XOR all → `a ^ b`. Take its lowest set bit (`x & -x`), split numbers into two groups by that bit, XOR each group.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 260 – [Single Number III](https://leetcode.com/problems/single-number-iii/) · GFG – "Non-Repeating Numbers"

---

## 4. Missing Number — `04_missing_number.py`
Numbers 0..n with one missing.

**Brute force:** For each candidate 0..n, scan the list for it.
Time **O(n²)** · Space **O(1)**

**Optimal:** XOR all indexes 0..n with all values. Or use the sum formula `n(n+1)/2 - total`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 268 – [Missing Number](https://leetcode.com/problems/missing-number/) · GFG – "Missing number in array"

---

## 5. Find the Difference — `05_find_the_difference.py`
`t` is `s` shuffled plus one extra letter.

**Brute force:** Count letters of `s` in a dict, then use them up while reading `t`.
Time **O(n)** · Space **O(1)** (at most 26 letters)

**Optimal:** XOR the `ord()` of every character in both strings, `chr()` the result.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 389 – [Find the Difference](https://leetcode.com/problems/find-the-difference/)

---

## 6. Single Element in a Sorted Array — `06_single_element_sorted_array.py`
Sorted, every element twice except one. Needs O(log n).

**Brute force:** XOR everything (ignores the sorting).
Time **O(n)** · Space **O(1)**

**Optimal:** Binary search on even indexes. If `nums[mid] == nums[mid+1]`, the single is to the right; otherwise it's at `mid` or to the left.
Time **O(log n)** · Space **O(1)**

**Equivalent questions:** LeetCode 540 – [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/) · GFG – "Find the element that appears once in a sorted array"
