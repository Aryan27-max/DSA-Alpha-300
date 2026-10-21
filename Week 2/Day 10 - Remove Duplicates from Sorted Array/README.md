# Day 10 · Remove Duplicates from Sorted Array
**Topic:** Two pointers same direction (read + write)

One pointer **reads** every element, another marks where the next "keeper" should be **written**. This idiom turns "delete stuff from a list" from O(n²) (every delete shifts everything) into a single O(n) pass. Swap instead of copy and you get Move Zeroes and partitioning; add a third pointer and you get the Dutch National Flag.

> No `list(set(nums))` or `list(dict.fromkeys(nums))`.

---

## 1. Remove Duplicates from Sorted Array (PRIMARY) — `01_remove_duplicates.py`

**Brute force:** When two neighbours match, `pop(i)` one of them. Each pop shifts the rest.
Time **O(n²)** · Space **O(1)**

**Optimal:** `write` starts at 1. If `nums[read] != nums[write-1]`, copy it to `nums[write]` and move `write`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 26 – [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · GFG – "Remove duplicates from sorted array"

---

## 2. Remove Duplicates from Sorted Array II — `02_remove_duplicates_ii.py`
Each value at most twice.

**Brute force:** Measure each run, pop extras.
Time **O(n²)** · Space **O(1)**

**Optimal:** Keep `nums[read]` if `write < 2` or it differs from `nums[write-2]`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 80 – [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

---

## 3. Remove Element — `03_remove_element.py`

**Brute force:** Pop every match.
Time **O(n²)** · Space **O(1)**

**Optimal:** Copy every non-`val` to `nums[write]`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 27 – [Remove Element](https://leetcode.com/problems/remove-element/) · GFG – "Remove all occurrences of an element from array"

---

## 4. Move Zeroes — `04_move_zeroes.py`
Zeros to the end, keep non-zero order.

**Brute force:** Copy non-zeros to a new list, pad with zeros, copy back.
Time **O(n)** · Space **O(n)**

**Optimal:** Swap every non-zero into `nums[write]`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 283 – [Move Zeroes](https://leetcode.com/problems/move-zeroes/) · GFG – "Move all zeroes to end of array"

---

## 5. Sort Array By Parity — `05_sort_array_by_parity.py`
Evens first, odds after.

**Brute force:** New list: append evens, then odds.
Time **O(n)** · Space **O(n)**

**Optimal:** Move Zeroes with the test "is it even?" — swap evens to `write`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 905 – [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) · GFG – "Segregate Even and Odd numbers"

---

## 6. Sort Colors — `06_sort_colors.py`
Sort 0s, 1s, 2s in one pass.

**Brute force:** Count each colour, then overwrite (two passes).
Time **O(n)** · Space **O(1)**

**Optimal:** Dutch National Flag with `low`, `mid`, `high`. On a 2, swap with `high` but don't advance `mid`.
Time **O(n)**, one pass · Space **O(1)**

**Equivalent questions:** LeetCode 75 – [Sort Colors](https://leetcode.com/problems/sort-colors/) · GFG – "Sort an array of 0s, 1s and 2s"
