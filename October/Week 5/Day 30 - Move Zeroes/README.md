# Day 30 · Move Zeroes
**Topic:** Two pointers revisit (read + write)

Consolidation day for in-place array work. The read/write idiom from Day 10 shows up again, plus its relatives: swap-with-the-end when order doesn't matter, pointers from both ends (the quicksort partition you'll write in November), a stable partition into three groups, and rotate-by-reversing. Everything in O(1) extra space unless the problem demands otherwise.

> No `nums.sort(key=lambda x: x == 0)`, no `filter()`, no `[x for x in nums if x != 0]` + padding. In place, O(1) extra space.

---

## 1. Move Zeroes (PRIMARY) — `01_move_zeroes.py`

**Brute force:** Bubble zeros right one adjacent swap at a time.
Time **O(n²)** · Space **O(1)**

**Optimal:** Read/write pointers; swap each non-zero into `nums[write]`. (Also included: copy non-zeros forward, then fill zeros.)
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 283 – [Move Zeroes](https://leetcode.com/problems/move-zeroes/) · GFG – "Move all zeroes to end of array"

---

## 2. Remove Element — `02_remove_element.py`
(Day 10 used read/write; today adds swap-with-end.)

**Brute force:** `pop(i)` every match.
Time **O(n²)** · Space **O(1)**

**Optimal (swap-to-end):** On a match, overwrite with the last element and shrink n; don't advance i.
Time **O(n)** · Space **O(1)** — fewer writes when `val` is rare (order not kept)

**Equivalent questions:** LeetCode 27 – [Remove Element](https://leetcode.com/problems/remove-element/)

---

## 3. Remove Duplicates from Sorted Array — `03_remove_duplicates_sorted.py`

**Brute force:** `pop(i)` when neighbours match.
Time **O(n²)** · Space **O(1)**

**Optimal (general template):** `keep_at_most(nums, k)` — keep `x` if `write < k` or `nums[write − k] != x`. k = 1 solves LC 26, k = 2 solves LC 80.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 26 – [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · LeetCode 80 – [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

---

## 4. Sort Array By Parity — `04_sort_array_by_parity.py`
(Day 10 used read/write; today uses pointers from both ends.)

**Brute force:** New list — evens, then odds.
Time **O(n)** · Space **O(n)**

**Optimal:** `left` finds a misplaced odd, `right` finds a misplaced even, swap. At most n/2 swaps.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 905 – [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) · GFG – "Segregate Even and Odd numbers"

---

## 5. Partition Array According to Given Pivot — `05_partition_array_by_pivot.py`

**Brute force:** Three lists (`<`, `==`, `>`), glued together.
Time **O(n)** · Space **O(n)** (three extra lists)

**Optimal:** One result array, one pass — fill `< pivot` from the front reading left→right, fill `> pivot` from the back reading right→left, pivot fills the middle. Stable.
Time **O(n)** · Space **O(n)** for the output only

**Equivalent questions:** LeetCode 2161 – [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/) · LeetCode 75 – [Sort Colors](https://leetcode.com/problems/sort-colors/) (unstable 3-way partition) · GFG – "Three way partitioning"

---

## 6. Rotate Array — `06_rotate_array.py`

**Brute force:** Rotate by one, k times.
Time **O(n·k)** · Space **O(1)**

**Extra array:** `moved[(i + k) % n] = nums[i]`.
Time **O(n)** · Space **O(n)**

**Optimal:** `k %= n`, then reverse all, reverse the first k, reverse the rest.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 189 – [Rotate Array](https://leetcode.com/problems/rotate-array/) · GFG – "Rotate Array"
