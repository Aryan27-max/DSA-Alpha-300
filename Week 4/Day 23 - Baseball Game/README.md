# Day 23 · Baseball Game
**Topic:** Stack as running state

When something only ever changes at its **end** — a score record, a text you're typing, a string where neighbours cancel — it's a stack. Today is about simulating a sequence with one, and keeping any totals updated as you push and pop instead of recomputing them. Final Prices also previews Day 26: "pop while the new value beats the top" is the monotonic stack.

> No `deque`, and no `sum(stack)` inside the loop — keep a running total.

---

## 1. Baseball Game (PRIMARY) — `01_baseball_game.py`

**Brute force:** Re-add the whole record after every operation.
Time **O(n²)** · Space **O(n)**

**Optimal:** Stack + running total (add on push, subtract on pop).
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 682 – [Baseball Game](https://leetcode.com/problems/baseball-game/) · LeetCode 150 – [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (same "simulate with a stack" shape) · GFG – "Evaluation of Postfix Expression"

---

## 2. Build an Array With Stack Operations — `02_build_array_with_stack_ops.py`

**Simulation:** Keep a real stack and compare its top with target.
Time **O(n)** · Space **O(n)**

**Optimal:** No stack needed — walk a pointer through target: always "Push", add "Pop" when the number isn't wanted.
Time **O(n)** · Space **O(1)** extra (output not counted)

**Equivalent questions:** LeetCode 1441 – [Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/)

---

## 3. Make The String Great — `03_make_the_string_great.py`

**Brute force:** Find the first bad pair, cut it, start over.
Time **O(n²)** · Space **O(n)**

**Optimal:** Stack — if the top and the new char differ only by case (`|ord diff| == 32`), pop; else push.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 1544 – [Make The String Great](https://leetcode.com/problems/make-the-string-great/)

---

## 4. Final Prices With a Special Discount — `04_final_prices_discount.py`

**Brute force:** For each item, scan forward for the first price ≤ it.
Time **O(n²)** · Space **O(1)** extra

**Optimal (monotonic stack):** Stack of indexes waiting for a discount. New price `p`: pop every waiting item with price ≥ `p` and subtract `p`. Push the new index.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 1475 – [Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) · GFG – "Next Smaller Element"

---

## 5. Remove All Adjacent Duplicates In String — `05_remove_adjacent_duplicates.py`

**Brute force:** Cut the first adjacent pair, repeat.
Time **O(n²)** · Space **O(n)**

**Optimal:** Stack — top equals new char → pop, else push.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 1047 – [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) · LeetCode 1209 – [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) · GFG – "Recursively remove all adjacent duplicates"

---

## 6. Backspace String Compare — `06_backspace_string_compare.py`
(Day 31 revisits this with the O(1)-space two-pointer version.)

**Brute force:** Real strings, slice off the last char on every `#`.
Time **O(n²)** · Space **O(n)**

**Optimal here:** Build each text with a stack (`#` = pop if not empty), compare.
Time **O(n + m)** · Space **O(n + m)**

**Equivalent questions:** LeetCode 844 – [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)
