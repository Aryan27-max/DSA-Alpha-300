# Week 2 · October DSA (Oct 8 – Oct 14)

| Day | Primary problem | Topic |
|---|---|---|
| 8 | Valid Palindrome | Two pointers from ends |
| 9 | Reverse String | In-place swap |
| 10 | Remove Duplicates from Sorted Array | Two pointers same direction (read + write) |
| 11 | Merge Sorted Array | Two pointers from the end (in-place merge) |
| 12 | Squares of a Sorted Array | Two pointers from both ends (compare absolute values) |
| 13 | Maximum Average Subarray I | Fixed-size sliding window |
| 14 | Contains Duplicate II | Sliding window + hashmap |

Each day folder has one `.py` file per problem (`01_` is always the primary, the rest are variants) and a `README.md` with brute force, optimal approach, complexity and the matching LeetCode / GFG questions.

**Run any file:** `python3 "Day 8 - Valid Palindrome/01_valid_palindrome.py"` — every file has small test cases at the bottom.

**No-libraries rule:** zero imports. No `sorted()` / `.sort()`, no `[::-1]` / `reversed()` / `.reverse()`, no `deque` or `heapq`.
- Sorting needs → hand-written merge sort, insertion sort, or counting sort.
- Merge k Sorted Lists → pairwise (tournament) merging instead of a heap.
- Moving Average → queue built from a list + head pointer, and a circular buffer.
- Linked-list problems → a small hand-made `ListNode` class in the file.
