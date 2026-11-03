# Day 13 · Maximum Average Subarray I
**Topic:** Fixed-size sliding window

The window-of-size-k template: build the first window, then slide — **add the one coming in, subtract the one going out**. The variants then loosen the rule: windows that grow and shrink (min subarray sum, longest substring, max ones with flips) and windows that track letter counts instead of a sum (anagrams).

> No `sum(nums[i:i+k])` inside the loop — that's O(n·k). Keep a running sum.

---

## 1. Maximum Average Subarray I (PRIMARY) — `01_max_average_subarray.py`

**Brute force:** Re-add every window of size k.
Time **O(n·k)** · Space **O(1)**

**Optimal:** Running window sum; each slide adds `nums[i]`, subtracts `nums[i-k]`. Divide by k once at the end.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 643 – [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) · GFG – "Find maximum average subarray of k length"

---

## 2. Max Sum Subarray of Size K (GFG) — `02_max_sum_subarray_size_k.py`

**Brute force:** Sum every window from scratch.
Time **O(n·k)** · Space **O(1)**

**Optimal:** The same sliding-window template, no division.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** GFG – "Max Sum Subarray of size K" · LeetCode 643 (same thing as an average)

---

## 3. Minimum Size Subarray Sum — `03_minimum_size_subarray_sum.py`

**Brute force:** From every start, extend until the sum reaches target.
Time **O(n²)** · Space **O(1)**

**Optimal:** Variable window — grow `right`, and while `sum >= target`, record the length and shrink `left`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 209 – [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) · GFG – "Smallest subarray with sum greater than x"

---

## 4. Longest Substring Without Repeating Characters — `04_longest_substring_without_repeating.py`

**Brute force:** From every start, grow with a set until a repeat.
Time **O(n²)** · Space **O(min(n, alphabet))**

**Optimal:** Dict of last-seen index. If `s[right]` was seen at or after `left`, jump `left` past it.
Time **O(n)** · Space **O(min(n, alphabet))**

**Equivalent questions:** LeetCode 3 – [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · GFG – "Longest Distinct Characters in String"

---

## 5. Find All Anagrams in a String — `05_find_all_anagrams.py`

**Brute force:** Count letters of every window from scratch and compare.
Time **O(n·m)** · Space **O(1)** (26 slots)

**Optimal:** Fixed window of size `len(p)` with 26-slot counts and a `matches` counter updated in O(1) per slide.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 438 – [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) · GFG – "Count Occurrences of Anagrams"

---

## 6. Kids With the Greatest Number of Candies — `06_kids_with_greatest_candies.py`

**Brute force:** For each kid, compare with every other kid.
Time **O(n²)** · Space **O(n)** for the output

**Optimal:** Find the max once, then check `candies[i] + extra >= max` for each kid.
Time **O(n)** · Space **O(n)** for the output

**Equivalent questions:** LeetCode 1431 – [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

---

## 7. Max Consecutive Ones III — `07_max_consecutive_ones_iii.py`

**Brute force:** From each start, extend until there are more than k zeros.
Time **O(n²)** · Space **O(1)**

**Optimal:** Longest window with at most k zeros: grow `right`, shrink `left` whenever zeros exceed k.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1004 – [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) · LeetCode 485 – [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) · GFG – "Maximize Number of 1's"
