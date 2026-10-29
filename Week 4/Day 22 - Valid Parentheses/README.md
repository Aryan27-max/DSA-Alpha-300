# Day 22 · Valid Parentheses
**Topic:** Stack-based matching

What *is* a stack? A plain list where you only touch the end: `append()` to push, `pop()` to pop, `[-1]` to peek. The last thing in is the first thing out — which is exactly how brackets close. Push openers, and on every closer check that the top is its partner. The variants turn the stack into a counter (one bracket type), a depth meter, a score accumulator, and a list of indexes.

> No `collections.deque`. The whole lesson is "what IS a stack" — a list is enough.

---

## 1. Valid Parentheses (PRIMARY) — `01_valid_parentheses.py`

**Brute force:** Keep deleting `()`, `[]`, `{}` until nothing changes; valid if you end with `""`.
Time **O(n²)** · Space **O(n)**

**Optimal:** Push openers; on a closer, the top must be its partner (else False), then pop. Stack must be empty at the end.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 20 – [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) · GFG – "Parenthesis Checker"

---

## 2. Minimum Add to Make Parentheses Valid — `02_min_add_to_make_valid.py`

**Stack version:** Push everything that can't be matched; answer = stack size.
Time **O(n)** · Space **O(n)**

**Optimal:** One bracket type → the stack only holds `(`, so keep counts instead: `open_count` and `close_needed`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 921 – [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) · GFG – "Minimum number of bracket reversals needed to make an expression balanced" (related)

---

## 3. Remove Outermost Parentheses — `03_remove_outermost_parentheses.py`

**Brute force:** Find each primitive piece with a balance counter, copy its inside.
Time **O(n)** · Space **O(n)**

**Optimal:** Depth counter in one pass — skip `(` at depth 0 and `)` that returns to depth 0.
Time **O(n)** · Space **O(1)** extra

**Equivalent questions:** LeetCode 1021 – [Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)

---

## 4. Score of Parentheses — `04_score_of_parentheses.py`

**Brute force:** Recursively split into top-level pieces; `()` = 1, `(A)` = 2·score(A).
Time **O(n²)** · Space **O(n)**

**Optimal (stack):** Each stack slot is a level's running score. On `)`, pop `inner` and add `1` or `2·inner` to the level below.
Time **O(n)** · Space **O(n)**

**Bonus:** Every `()` at depth d is worth 2^d — add those up with O(1) space.

**Equivalent questions:** LeetCode 856 – [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)

---

## 5. Longest Valid Parentheses — `05_longest_valid_parentheses.py`

**Brute force:** From each start, extend while balance ≥ 0; record lengths where balance = 0.
Time **O(n²)** · Space **O(1)**

**Optimal:** Stack of indexes with a floor (start with `-1`). On `)`, pop; if empty, push `i` as the new floor; else length = `i − stack[-1]`.
Time **O(n)** · Space **O(n)**

**Bonus:** Two counter passes (left→right and right→left) — O(1) space.

**Equivalent questions:** LeetCode 32 – [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) · GFG – "Longest valid Parentheses"

---

## 6. Minimum Remove to Make Valid Parentheses — `06_min_remove_to_make_valid.py`

**Brute force:** BFS — remove 0, then 1, then 2 parentheses… return the first valid string.
Time **exponential** · Space **exponential**

**Optimal:** Stack of `(` indexes. Unmatched `)` → mark; leftover `(` in the stack → mark. Rebuild skipping marks.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 1249 – [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) · LeetCode 301 – [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) (all answers, uses the BFS idea)
