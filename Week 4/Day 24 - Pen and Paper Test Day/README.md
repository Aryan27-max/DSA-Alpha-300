# Day 24 · Pen & Paper Test Day ⚡
**No new problem today.** Three problems are picked from Days 1–23 and solved on paper.

| Block | Time | What happens |
|---|---|---|
| Write | 90 min | Solve 3 problems on paper — no laptop, no running code |
| Peer-trace | 90 min | Swap papers; trace your partner's code by hand on **new** inputs |
| Walkthrough | 60 min | Explain one solution out loud, start to finish |

---

## How to prepare

1. **Re-write primaries from memory.** For each primary from Days 1–23, write the optimal code on paper without looking, then compare with the `01_` file in that day's folder.
2. **Say the pattern out loud in one line**, e.g. "Two Sum: dict of value → index, look up `target − x`."
3. **Know your complexities cold** — time *and* space, and why.
4. **Practise tracing.** Pick an input, keep a little table of every variable after each loop step. That's exactly what the peer-trace block checks.
5. **Remember the October rules on paper too:** no `Counter`, `deque`, `sorted()`, `[::-1]`, `accumulate`, etc.

---

## Three mock papers to practise with

Each mock mixes three different patterns. Give yourself 90 minutes per mock.

**Mock A**
1. Two Sum (Day 1) — hashmap lookup
2. Remove Duplicates from Sorted Array (Day 10) — read/write pointers
3. Valid Parentheses (Day 22) — stack

**Mock B**
1. Majority Element — both hashmap **and** Boyer-Moore (Day 5)
2. Merge Sorted Array (Day 11) — three pointers from the end
3. Find Pivot Index (Day 20) — prefix sum split point

**Mock C**
1. Find All Numbers Disappeared in an Array (Day 6) — in-place marking
2. Longest Substring Without Repeating Characters (Day 13) — variable window
3. Isomorphic Strings (Day 19) — two dicts (explain why one isn't enough)

**Stretch set** (if you finish early): Single Number II (Day 3), Minimum Window Substring (Day 15), Longest Valid Parentheses (Day 22).

---

## Tricky inputs for the peer-trace block

Use these to break your partner's code (and test your own):

| Problem | Inputs worth tracing |
|---|---|
| Two Sum | `[3, 3]`, target 6 (same value twice) · negatives `[-1, -2, -3]`, target −5 |
| Contains Duplicate II | `k = 0` · duplicate exactly `k` apart vs `k + 1` apart |
| Single Number | `[0]` · negatives `[-1, -1, -2]` |
| Majority Element (GFG) | no majority: `[1, 2, 3]` · all equal: `[7, 7, 7]` |
| Remove Duplicates | `[]` · `[1]` · `[2, 2, 2, 2]` |
| Merge Sorted Array | `m = 0` · `n = 0` · all of nums2 smaller than nums1 |
| Squares of Sorted Array | all negative `[-5, -3, -1]` · zeros mixed in |
| Valid Palindrome | `" "` · `"0P"` (digit vs letter) · `".,"` |
| Max Average Subarray | `k = len(nums)` · all negatives |
| Valid Anagram | different lengths · same letters, different counts `"aab"` vs `"abb"` |
| Isomorphic Strings | `"badc"` / `"baba"` (catches the one-dict bug) |
| Find Pivot Index | pivot at index 0 `[2, 1, -1]` · no pivot `[1, 2, 3]` |
| Valid Parentheses | `"("` · `")"` · `"([)]"` · `""` |
| Backspace Compare | more `#` than letters `"a##c"` · `#` at the start |

---

## Walkthrough checklist

When you explain a solution out loud, hit these in order:

1. **Restate the problem** in your own words, with one small example.
2. **Brute force first** — what it is and its complexity.
3. **The key insight** — the one sentence that makes the optimal solution work.
4. **Walk the code** line by line on a small input.
5. **Edge cases** — empty input, one element, duplicates, negatives.
6. **Complexity** — time and space, and where each comes from.

---

**Equivalent practice:** the `01_` primary file in every folder from Day 1 to Day 23 · LeetCode problem lists by tag (Array, Hash Table, Two Pointers, Sliding Window, String, Prefix Sum, Stack).
