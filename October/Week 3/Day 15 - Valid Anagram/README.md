# Day 15 · Valid Anagram
**Topic:** Character frequency counting

Two strings are anagrams when their **letter counts** match — order doesn't matter. That one idea powers today's whole set: use the counts as a dict key (grouping), keep them over a sliding window (find anagrams, permutations), cover a target (minimum window), or go one level up and count the counts (close strings).

> No `Counter(s) == Counter(t)` and no `sorted(s) == sorted(t)`. Build dicts by hand.

---

## 1. Valid Anagram (PRIMARY) — `01_valid_anagram.py`

**Brute force:** For each letter in `s`, find and remove a matching letter from `t`.
Time **O(n²)** · Space **O(n)**

**Optimal:** Two count dicts compared key by key — or one "balance" dict (+1 for `s`, −1 for `t`) that must end all zeros.
Time **O(n)** · Space **O(1)** (at most 26 keys for lowercase letters)

**Equivalent questions:** LeetCode 242 – [Valid Anagram](https://leetcode.com/problems/valid-anagram/) · GFG – "Anagram"

---

## 2. Group Anagrams — `02_group_anagrams.py`

**Brute force:** Compare each word against the first word of every existing group.
Time **O(n²·L)** · Space **O(n·L)**

**Optimal:** Signature = tuple of 26 letter counts; dict from signature to list of words.
Time **O(n·L)** · Space **O(n·L)**

**Equivalent questions:** LeetCode 49 – [Group Anagrams](https://leetcode.com/problems/group-anagrams/) · GFG – "Print Anagrams Together"

---

## 3. Find All Anagrams in a String — `03_find_all_anagrams.py`
(Third version: Day 13 used arrays + `matches`, Day 14 used `need` + `missing`, today uses one balance dict + `nonzero`.)

**Brute force:** Run the anagram check on every window.
Time **O(n·m)** · Space **O(alphabet)**

**Optimal:** Balance dict starts with `p`'s letters at +1. Entering letter −1, leaving letter +1. `nonzero == 0` → anagram.
Time **O(n)** · Space **O(alphabet)**

**Equivalent questions:** LeetCode 438 – [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) · GFG – "Count Occurrences of Anagrams"

---

## 4. Permutation in String — `04_permutation_in_string.py`

**Brute force:** Count every window from scratch.
Time **O(n·m)** · Space **O(26)**

**Optimal:** Two 26-slot count lists, slide the window, compare the lists (26 comparisons = constant).
Time **O(26·n) = O(n)** · Space **O(26)**

**Equivalent questions:** LeetCode 567 – [Permutation in String](https://leetcode.com/problems/permutation-in-string/) · GFG – "Check if a string contains an anagram of another string"

---

## 5. Minimum Window Substring — `05_minimum_window_substring.py`

**Brute force:** From every start, grow until the window covers `t`.
Time **O(n²·k)** · Space **O(k)**

**Optimal:** `need` dict + `missing` counter. Grow right until `missing == 0`, then shrink left while still covered, recording the shortest window.
Time **O(|s| + |t|)** · Space **O(alphabet)**

**Equivalent questions:** LeetCode 76 – [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) · GFG – "Smallest window in a string containing all the characters of another string"

---

## 6. Determine if Two Strings Are Close — `06_determine_two_strings_close.py`

**Brute force:** Check same letter set, then insertion-sort both count lists and compare.
Time **O(n + 26²)** · Space **O(26)**

**Optimal:** Same letter set **and** same "count of counts" dict.
Time **O(n)** · Space **O(26)**

**Equivalent questions:** LeetCode 1657 – [Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/)
