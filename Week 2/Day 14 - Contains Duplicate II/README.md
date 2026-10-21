# Day 14 · Contains Duplicate II
**Topic:** Sliding window + hashmap

This day ties the two weeks together: Week 1's "have I seen it?" hashing, plus Week 2's sliding window. Instead of "have I *ever* seen it?", the question becomes "have I seen it **in the last k steps**?". The variants keep a window of counts (permutations, anagrams, character replacement), buckets (near-duplicates), or a running sum over a stream.

> No `Counter`, no `deque`. Rolling dicts and windows are built and updated inline.

---

## 1. Contains Duplicate II (PRIMARY) — `01_contains_duplicate_ii.py`

**Brute force:** Compare each number with the next k numbers.
Time **O(n·k)** · Space **O(1)**

**Optimal (two versions):**
- Rolling dict of last-seen index — Time **O(n)** · Space **O(n)**
- Window set of the last k values (add new, discard `nums[i-k]`) — Time **O(n)** · Space **O(k)**

**Equivalent questions:** LeetCode 219 – [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) · GFG – "Check if array contains duplicates within k distance"

---

## 2. Contains Duplicate III — `02_contains_duplicate_iii.py`

**Brute force:** Compare each number with the next `indexDiff` numbers.
Time **O(n·indexDiff)** · Space **O(1)**

**Optimal:** Buckets of width `valueDiff + 1` in a dict, keeping only the last `indexDiff` values. Same bucket → True; neighbour bucket → check the difference.
Time **O(n)** · Space **O(min(n, indexDiff))**

**Equivalent questions:** LeetCode 220 – [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)

---

## 3. Permutation in String — `03_permutation_in_string.py`

**Brute force:** Build a count dict for every window of s2 and compare with s1's.
Time **O(n·m)** · Space **O(alphabet)**

**Optimal:** Fixed window with a `need` dict and a `missing` counter. Letter in: if it was needed, `missing -= 1`. Letter out: if that creates a need again, `missing += 1`. `missing == 0` → found.
Time **O(n)** · Space **O(alphabet)**

**Equivalent questions:** LeetCode 567 – [Permutation in String](https://leetcode.com/problems/permutation-in-string/) · GFG – "Check if a string contains an anagram of another string"

---

## 4. Find All Anagrams in a String — `04_find_all_anagrams.py`
(Day 13 used 26-slot arrays; this one uses the dict + `missing` window so it works for any characters.)

**Brute force:** Rebuild a count dict for every window.
Time **O(n·m)** · Space **O(alphabet)**

**Optimal:** Permutation in String's window, but collect every start index where `missing == 0`.
Time **O(n)** · Space **O(alphabet)**

**Equivalent questions:** LeetCode 438 – [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) · GFG – "Count Occurrences of Anagrams"

---

## 5. Longest Repeating Character Replacement — `05_longest_repeating_char_replacement.py`

**Brute force:** Every start, grow while `length − most common count ≤ k`.
Time **O(n²)** · Space **O(26)**

**Optimal:** Window with letter counts and `max_freq`. If `window − max_freq > k`, slide `left` by one. `max_freq` never needs lowering.
Time **O(n)** · Space **O(26)**

**Equivalent questions:** LeetCode 424 – [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) · LeetCode 1004 – [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) (same window shape)

---

## 6. Moving Average from Data Stream — `06_moving_average_data_stream.py`

**Brute force:** Store everything and re-add the last `size` values on every call.
Time **O(size) per call** · Space **O(n)**

**Optimal:** Running sum + a hand-built queue. Two versions: a list with a `head` pointer, and a fixed circular buffer (`count % size`).
Time **O(1) per call** · Space **O(size)** (circular buffer)

**Equivalent questions:** LeetCode 346 – [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) · LeetCode 643 – [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) (free, same running-sum window) · LeetCode 933 – [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) (free, list-as-queue window)
