# Day 5 · Majority Element
**Topic:** Hashmap counting + Boyer-Moore

Two ways to solve the same problem: count everything with a dict (easy, uses memory) or Boyer-Moore voting (clever, uses no memory). The point of today is that **picking the algorithm matters** — and that when input is sorted, binary search can beat both.

> No `Counter.most_common()`, no `statistics.mode()`. Both the hashmap and Boyer-Moore versions are hand-built in the primary file.

---

## 1. Majority Element (PRIMARY) — `01_majority_element.py`
Element appearing more than n/2 times (guaranteed to exist).

**Brute force:** For each element, count its copies with an inner loop.
Time **O(n²)** · Space **O(1)**

**Hashmap:** Count in a dict, return when a count crosses n/2.
Time **O(n)** · Space **O(n)**

**Optimal – Boyer-Moore:** Keep a candidate and a count. Same → +1, different → −1, count hits 0 → new candidate.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 169 – [Majority Element](https://leetcode.com/problems/majority-element/) · GFG – "Majority Element"

---

## 2. Majority Element II — `02_majority_element_ii.py`
All elements appearing more than n/3 times (there are at most 2).

**Brute force:** Dict counting.
Time **O(n)** · Space **O(n)**

**Optimal:** Boyer-Moore with two candidates, then a second pass to verify their counts.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 229 – [Majority Element II](https://leetcode.com/problems/majority-element-ii/) · GFG – "Majority Vote" (more than n/3)

---

## 3. Element Appearing More Than 25% in Sorted Array — `03_element_more_than_25_percent.py`

**Brute force / simple:** Walk once; if `arr[i] == arr[i + n//4]`, that's the answer.
Time **O(n)** · Space **O(1)**

**Optimal:** Only `arr[n/4]`, `arr[n/2]`, `arr[3n/4]` can be the answer. For each, binary search its first and last position and check the block length.
Time **O(log n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1287 – [Element Appearing More Than 25% In Sorted Array](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/) · GFG – "Number of occurrence" (first/last occurrence binary search)

---

## 4. Check If a Number Is Majority Element in a Sorted Array — `04_check_majority_sorted.py`

**Brute force:** Count `target` with a loop.
Time **O(n)** · Space **O(1)**

**Optimal:** Binary search the first index `i` of `target`. It's a majority only if `nums[i + n//2] == target`.
Time **O(log n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1150 – [Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Premium) · LeetCode 34 – [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (free version of the same skill)

---

## 5. Degree of an Array — `05_degree_of_an_array.py`
Shortest subarray with the same max frequency as the whole array.

**Brute force:** Check every subarray, compute its degree.
Time **O(n³)** · Space **O(n)**

**Optimal:** One pass storing `count`, `first index`, `last index` for every value. For values with max count, answer is the smallest `last − first + 1`.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 697 – [Degree of an Array](https://leetcode.com/problems/degree-of-an-array/)

---

## 6. Majority Element (GFG) — `06_majority_element_gfg.py`
Like the primary, but the majority might not exist → return -1.

**Brute force:** Dict counting.
Time **O(n)** · Space **O(n)**

**Optimal:** Boyer-Moore for a candidate, then a second pass to verify it really appears more than n/2 times.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** GFG – "Majority Element" · LeetCode 169 (guaranteed version)
