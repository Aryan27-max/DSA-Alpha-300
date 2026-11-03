# Week 4 · October DSA (Oct 22 – Oct 28)
**Theme:** Stacks + Queues — LIFO / FIFO · bracket matching · monotonic stack intro

| Day | Primary problem | Topic |
|---|---|---|
| 22 | Valid Parentheses | Stack-based matching |
| 23 | Baseball Game | Stack as running state |
| 24 | ⚡ Pen & Paper Test Day | 3 problems from Days 1–23 (see the folder's README for mock papers + trace inputs) |
| 25 | Min Stack | Augmented stack (2nd stack for min) |
| 26 | Next Greater Element I | Monotonic decreasing stack |
| 27 | Implement Queue using Stacks | Two-stack FIFO simulation |
| 28 | Number of Recent Calls | Monotonic queue (sliding window of time) |

Each day folder has one `.py` file per problem (`01_` is always the primary, the rest are variants) and a `README.md` with brute force, optimal approach, complexity and the matching LeetCode / GFG questions.

**Run any file:** `python3 "Day 22 - Valid Parentheses/01_valid_parentheses.py"` — every file has small test cases at the bottom.

**No-libraries rule:** zero imports. No `deque`, `heapq`, `bisect`, `sorted()` or `[::-1]`.
- Stacks are plain lists (`append` / `pop` / `[-1]`).
- Queues are hand-built: two stacks, a list + head pointer, or a fixed circular buffer.
- Design Twitter merges followees' tweets by scanning stack tops (no heap until December).

**Sliding Window Maximum appears three times, solved three ways:**
Day 25 two max-stacks → Day 26 monotonic deque (list + head) → Day 28 monotonic deque in a k-slot ring.
**Moving Average** likewise: Day 14 ring → Day 27 two-stack queue → Day 28 `pop(0)` vs ring.
