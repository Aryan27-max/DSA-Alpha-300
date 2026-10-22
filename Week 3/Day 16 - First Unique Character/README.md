# Day 16 · First Unique Character in a String
**Topic:** Freq map + ordered scan

The two-pass habit: **build a map first, then query it**. Pass 1 counts; pass 2 walks the original string (or a fixed a–z order) and asks the map questions. The variants show when one pass is enough (first repeat in a stream), and how counts can be bucketed to "sort" without sorting.

> No `Counter(s)` and no `OrderedDict`. Plain dict + two loops.

---

## 1. First Unique Character in a String (PRIMARY) — `01_first_unique_character.py`

**Brute force:** For every character, scan the whole string for another copy.
Time **O(n²)** · Space **O(1)**

**Optimal:** Count in a dict, then walk the string and return the first index whose count is 1.
Time **O(n)** · Space **O(1)** (at most 26 keys)

**Equivalent questions:** LeetCode 387 – [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) · GFG – "Non Repeating Character"

---

## 2. Find the Difference — `02_find_the_difference.py`
(Day 3 used XOR; this is the frequency-map version.)

**Brute force:** For each letter of `t`, count it in `s` and in `t`.
Time **O(n²)** · Space **O(1)**

**Optimal:** Fill a bag (dict) with `s`, take `t`'s letters out; the first one you can't take out is the extra.
Time **O(n)** · Space **O(26)**

**Equivalent questions:** LeetCode 389 – [Find the Difference](https://leetcode.com/problems/find-the-difference/)

---

## 3. First Letter to Appear Twice — `03_first_letter_to_appear_twice.py`

**Brute force:** For each position, look back for an earlier copy.
Time **O(n²)** · Space **O(1)**

**Optimal:** One pass with a set; return the first letter already in it.
Time **O(n)** · Space **O(26)**

**Equivalent questions:** LeetCode 2351 – [First Letter to Appear Twice](https://leetcode.com/problems/first-letter-to-appear-twice/) · GFG – "Find the first repeated character in a string"

---

## 4. Unique Number of Occurrences — `04_unique_number_of_occurrences.py`

**Brute force:** Count, then compare every pair of counts.
Time **O(n + d²)** · Space **O(d)** (d = distinct values)

**Optimal:** Count, then push each count into a set; a repeat means False.
Time **O(n)** · Space **O(d)**

**Equivalent questions:** LeetCode 1207 – [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)

---

## 5. Sort Characters By Frequency — `05_sort_characters_by_frequency.py`

**Brute force:** Repeatedly pick the character with the highest remaining count.
Time **O(n + d²)** · Space **O(n)**

**Optimal:** Bucket sort — `buckets[c]` holds characters seen exactly `c` times; walk buckets from high to low.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 451 – [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) · LeetCode 1636 – [Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) · GFG – "Sorting Elements of an Array by Frequency"

---

## 6. Increasing Decreasing String — `06_increasing_decreasing_string.py`

**Brute force:** For every pick, search the remaining characters for the next bigger / smaller one.
Time **O(n²)** · Space **O(n)**

**Optimal:** 26-slot count list (already in alphabet order). Sweep a→z then z→a, taking one of each available letter, until everything is placed.
Time **O(26 · n)** worst = **O(n)** · Space **O(26)**

**Equivalent questions:** LeetCode 1370 – [Increasing Decreasing String](https://leetcode.com/problems/increasing-decreasing-string/)
