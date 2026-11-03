# Week 3 · October DSA (Oct 15 – Oct 21)
**Theme:** Strings + Prefix Sum — character counting · index arithmetic · cumulative sums

| Day | Primary problem | Topic |
|---|---|---|
| 15 | Valid Anagram | Character frequency counting |
| 16 | First Unique Character in a String | Freq map + ordered scan |
| 17 | Longest Common Prefix | Vertical scan / horizontal scan |
| 18 | Reverse Words in a String III | String split + in-place reverse |
| 19 | Isomorphic Strings | Bijective hashmap (two dicts) |
| 20 | Find Pivot Index | Prefix sum — split point |
| 21 | Range Sum Query – Immutable | Prefix sum — static range queries |

Each day folder has one `.py` file per problem (`01_` is always the primary, the rest are variants) and a `README.md` with brute force, optimal approach, complexity and the matching LeetCode / GFG questions.

**Run any file:** `python3 "Day 15 - Valid Anagram/01_valid_anagram.py"` — every file has small test cases at the bottom.

**No-libraries rule:** zero imports. No `Counter`, `OrderedDict`, `sorted()`, `[::-1]`, `accumulate`, `takewhile`, `commonprefix` or `zip(*strs)`.
- Substring search (Rotate String, Repeated Substring Pattern) → hand-written KMP.
- Frequency "sorting" → bucket sort and 26-slot count arrays.
- Range Sum Query – Mutable → hand-built Fenwick tree.

**Problems you've met before** are solved from a new angle so you learn something each time:
- Find All Anagrams: Day 13 (arrays + matches) → Day 14 (`need` + `missing`) → Day 15 (balance dict + `nonzero`).
- Find the Difference: Day 3 (XOR) → Day 16 (frequency bag).
- Rotate String: Day 17 (KMP on `s + s`) → Day 19 (index mapping).
- Buddy Strings: Day 17 (mismatch indexes) → Day 19 (mismatch pairs as a mapping).
