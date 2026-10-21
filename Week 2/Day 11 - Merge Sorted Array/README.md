# Day 11 · Merge Sorted Array
**Topic:** Two pointers from the end (in-place merge)

When you merge into an array that already holds data, writing from the front overwrites values you still need. Writing from the **back** — into the empty space — avoids that completely. Merging is also the heart of merge sort, which you'll build properly in November.

> No `sorted(nums1 + nums2)` or `heapq.merge()`. Merge Intervals uses a hand-written merge sort; Merge k Lists uses pairwise merging instead of a heap.

---

## 1. Merge Sorted Array (PRIMARY) — `01_merge_sorted_array.py`

**Brute force:** Merge from the front into a new list, then copy back.
Time **O(m+n)** · Space **O(m+n)**

**Optimal:** Three pointers from the end (`i` in nums1, `j` in nums2, `w` for writing). Place the bigger value at `w`. Stop when nums2 is used up.
Time **O(m+n)** · Space **O(1)**

**Equivalent questions:** LeetCode 88 – [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) · GFG – "Merge Without Extra Space"

---

## 2. Merge Two Sorted Lists — `02_merge_two_sorted_lists.py`

**Recursive:** Smaller head wins; recurse on the rest.
Time **O(n+m)** · Space **O(n+m)** call stack

**Optimal:** Dummy node + tail pointer, attach the smaller node each step, attach the leftovers at the end.
Time **O(n+m)** · Space **O(1)**

**Equivalent questions:** LeetCode 21 – [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) · GFG – "Merge two sorted linked lists"

---

## 3. Merge k Sorted Lists — `03_merge_k_sorted_lists.py`

**Brute force:** Merge lists one by one into a growing result.
Time **O(N·k)** · Space **O(1)** (N = total nodes)

**Optimal (no heap):** Merge in pairs, round after round, until one list is left.
Time **O(N log k)** · Space **O(k)** for the list of heads

**Equivalent questions:** LeetCode 23 – [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) · GFG – "Merge K sorted linked lists"

---

## 4. Merge Intervals — `04_merge_intervals.py`

**Brute force:** Keep merging any overlapping pair until nothing changes.
Time **O(n³)** worst · Space **O(n)**

**Optimal:** Merge-sort by start, then one pass: overlap with the last merged one → stretch its end; otherwise add a new one.
Time **O(n log n)** · Space **O(n)**

**Equivalent questions:** LeetCode 56 – [Merge Intervals](https://leetcode.com/problems/merge-intervals/) · GFG – "Overlapping Intervals"

---

## 5. Insert Interval — `05_insert_interval.py`

**Brute force:** Append the new interval, sort, run full Merge Intervals.
Time **O(n log n)** (O(n²) with the insertion sort used) · Space **O(n)**

**Optimal:** Already sorted, so three phases in one pass: copy the left ones, swallow the overlapping ones, copy the right ones.
Time **O(n)** · Space **O(n)** for the output

**Equivalent questions:** LeetCode 57 – [Insert Interval](https://leetcode.com/problems/insert-interval/) · GFG – "Insert Interval"

---

## 6. Decompress Run-Length Encoded List — `06_decompress_rle_list.py`

**Brute force:** `result = result + [val] * freq` for every pair (copies the whole result each time).
Time **O(L²)** worst · Space **O(L)** (L = output length)

**Optimal:** Read pairs two at a time, append `val` `freq` times.
Time **O(L)** · Space **O(L)** for the output

**Equivalent questions:** LeetCode 1313 – [Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/) · GFG – "Run Length Encoding" (the compress direction)
