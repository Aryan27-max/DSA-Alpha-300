# Day 31 · Backspace String Compare
**Topic:** Stacks revisit (two stacks compared)

The last day of October. Build two stacks with a simulated backspace and compare — then the bonus: read both strings **backwards** with a skip counter and use O(1) space. The variants revisit stacks from every angle this month: folder paths, cancelling pairs (with the stack living inside the array), a greedy monotonic stack, a stack that reverses for free, and a backwards walk over a run-length tape.

> No `deque`. A list is the stack. Bonus: O(1) space with two reverse pointers.

---

## 1. Backspace String Compare (PRIMARY) — `01_backspace_string_compare.py`

**Stacks (Day 23 version):** Build both texts (`#` = pop), compare.
Time **O(n + m)** · Space **O(n + m)**

**Optimal (bonus):** Two pointers from the end; a skip counter erases characters as you meet `#`. Compare survivors one by one.
Time **O(n + m)** · Space **O(1)**

**Equivalent questions:** LeetCode 844 – [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

---

## 2. Simplify Path — `02_simplify_path.py`

**With `split('/')`:** Stack of folder names — push names, pop on `..`, skip `.` and empties.
Time **O(n)** · Space **O(n)**

**Without split:** Walk the characters, skip slash runs, read each name by index — same stack logic.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 71 – [Simplify Path](https://leetcode.com/problems/simplify-path/) · GFG – "Simplify the directory path (Unix like)"

---

## 3. Remove All Adjacent Duplicates In String — `03_remove_adjacent_duplicates.py`
(Day 23 used a separate stack; today the stack lives inside the char array.)

**Brute force:** Cut the first adjacent pair, repeat.
Time **O(n²)** · Space **O(n)**

**Optimal:** `chars[0..write−1]` is the stack. Copy `chars[read]` to `chars[write]`; if it equals the one below, `write −= 1`, else `write += 1`.
Time **O(n)** · Space **O(1)** extra beyond the char list

**Equivalent questions:** LeetCode 1047 – [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) · LeetCode 1209 – [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

---

## 4. Remove K Digits — `04_remove_k_digits.py`

**Brute force:** k times, try removing each digit and keep the smallest result.
Time **O(k · n²)** · Space **O(n)**

**Optimal (greedy monotonic stack):** Pop while `k > 0` and the top is bigger than the new digit. Leftover k → pop from the end. Strip leading zeros.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 402 – [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) · LeetCode 316 – [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) · GFG – "Build the smallest number by removing k digits"

---

## 5. Reverse Only Letters — `05_reverse_only_letters.py`
(Day 8 and Day 18 used two pointers; today shows the stack version beside it.)

**Brute force:** For the k-th letter, count from the right to find its mirror.
Time **O(n²)** · Space **O(n)**

**Stack version:** Push all letters, then pop one at each letter position.
Time **O(n)** · Space **O(n)**

**Optimal:** Two-pointer swap skipping non-letters.
Time **O(n)** · Space **O(n)** for the char list only

**Equivalent questions:** LeetCode 917 – [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/) · GFG – "Reverse a string without affecting special characters"

---

## 6. Decoded String at Index — `06_decoded_string_at_index.py`

**Brute force:** Build the tape until it reaches length k.
Time/Space **O(k)** — impossible when k is ~10⁹

**Optimal:** Pass 1 computes the tape length. Pass 2 walks backwards: `k %= size`; a letter with `k == 0` is the answer; undo digits with `size //= d` and letters with `size −= 1`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 880 – [Decoded String at Index](https://leetcode.com/problems/decoded-string-at-index/) · LeetCode 394 – [Decode String](https://leetcode.com/problems/decode-string/) (stack-based decoding)
