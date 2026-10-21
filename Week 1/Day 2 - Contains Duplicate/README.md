# Day 2 · Contains Duplicate
**Topic:** Set membership

The most basic question in hashing: *"Have I seen this before?"* A set answers it in O(1). The variants push the idea further — add a distance limit, add a value tolerance, or use the array itself as the "set" to save memory.

---

## 1. Contains Duplicate (PRIMARY) — `01_contains_duplicate.py`
Is there any value that shows up twice?

**Brute force:** Compare every pair.
Time **O(n²)** · Space **O(1)**

**Optimal:** Walk the list with a set. If the number is already in the set → return True right away (don't keep reading).
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 217 – [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) · GFG – "Check if array contains duplicates"

---

## 2. Contains Duplicate II — `02_contains_duplicate_ii.py`
Same value, and indexes at most `k` apart.

**Brute force:** For each index, look ahead up to `k` places.
Time **O(n·k)** · Space **O(1)**

**Optimal:** Dict of `value -> last index seen`. When you see a value again, check the gap.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 219 – [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) · GFG – "Check duplicates within k distance"

---

## 3. Contains Duplicate III — `03_contains_duplicate_iii.py`
Indexes at most `indexDiff` apart **and** values at most `valueDiff` apart.

**Brute force:** For each index, compare with the next `indexDiff` elements.
Time **O(n·indexDiff)** · Space **O(1)**

**Optimal:** Buckets of width `valueDiff + 1`. Same bucket → close enough. Neighbour bucket → check it. Keep only the last `indexDiff` numbers in the buckets.
Time **O(n)** · Space **O(min(n, indexDiff))**

**Equivalent questions:** LeetCode 220 – [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)

---

## 4. Find All Duplicates in an Array — `04_find_all_duplicates.py`
Values are 1..n, each appears once or twice. Return the ones that appear twice, in O(1) extra space.

**Brute force:** Count with a dict, return counts of 2.
Time **O(n)** · Space **O(n)**

**Optimal:** For value `v`, flip `nums[v-1]` negative. If it's already negative, `v` is a duplicate.
Time **O(n)** · Space **O(1)** (not counting the output)

**Equivalent questions:** LeetCode 442 – [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) · GFG – "Find duplicates in an array"

---

## 5. First Repeating Element (GFG) — `05_first_repeating_element.py`
1-based position of the first element that repeats somewhere.

**Brute force:** For each element, scan the rest for a copy.
Time **O(n²)** · Space **O(1)**

**Optimal:** Count everything in a dict, then walk from the left and return the first one with count > 1.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** GFG – "First Repeating Element" · LeetCode 387 – [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (same two-pass counting idea)

---

## 6. Duplicate Zeros — `06_duplicate_zeros.py`
Write every 0 twice, shifting the rest right, in place.

**Brute force:** On every 0, shift the rest of the array right by one.
Time **O(n²)** · Space **O(1)**

**Optimal:** Count zeros, then fill from the back with two pointers (one in the real array, one in the "stretched" array).
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1089 – [Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)
