# Day 17 · Longest Common Prefix
**Topic:** Vertical scan / horizontal scan

Line the words up and read them **column by column** — stop at the first column that disagrees. That's the vertical scan, and it's the same shape a trie takes later in December. The variants are all about comparing strings carefully by index: across many words, against a prefix, against rotations, against one swap, and against a repeating block (with a hand-written KMP).

> No `os.path.commonprefix()`, `itertools.takewhile()`, or `zip(*strs)` + set tricks. Walk the characters by index and bail on the first mismatch.

---

## 1. Longest Common Prefix (PRIMARY) — `01_longest_common_prefix.py`

**Horizontal scan:** Start with the first word as the prefix; shrink it against each next word.
Time **O(S)** (S = total characters) · Space **O(1)**

**Optimal — vertical scan:** Check column 0 of every word, then column 1, …; stop at the first mismatch or the first word that runs out.
Time **O(S)** worst, but stops after `n · (prefix length + 1)` checks · Space **O(1)**

**Equivalent questions:** LeetCode 14 – [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) · GFG – "Longest Common Prefix in an Array"

---

## 2. Find Common Characters — `02_find_common_characters.py`

**Brute force:** For each letter of the first word, remove one copy from every other word if they all have it.
Time **O(k · L²)** · Space **O(k · L)**

**Optimal:** 26-slot counts per word; keep the minimum for each letter.
Time **O(k · L)** · Space **O(26)**

**Equivalent questions:** LeetCode 1002 – [Find Common Characters](https://leetcode.com/problems/find-common-characters/) · GFG – "Common characters in n strings"

---

## 3. Check If a Word Occurs As a Prefix of Any Word — `03_word_occurs_as_prefix.py`

**Brute force:** `split()` the sentence and compare each word's first letters by index.
Time **O(n)** · Space **O(n)** for the word list

**Optimal:** One walk over the sentence; at each word start compare with `searchWord`, otherwise skip to the next space.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1455 – [Check If a Word Occurs As a Prefix of Any Word in a Sentence](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/) · LeetCode 2185 – [Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/)

---

## 4. Rotate String — `04_rotate_string.py`

**Brute force:** Try all n shifts, compare with `(i + shift) % n`.
Time **O(n²)** · Space **O(1)**

**Optimal:** Every rotation lives inside `s + s`. Check equal length, then search `goal` in `s + s` with hand-written KMP.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 796 – [Rotate String](https://leetcode.com/problems/rotate-string/) · GFG – "Check if strings are rotations of each other or not" · LeetCode 28 – [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) (KMP practice)

---

## 5. Buddy Strings — `05_buddy_strings.py`

**Brute force:** Try every swap and compare.
Time **O(n³)** · Space **O(n)**

**Optimal:** Collect differing positions. Exactly 2 that cross → True. 0 differences → True only if some letter repeats. Otherwise False.
Time **O(n)** · Space **O(1)** (26-letter set)

**Equivalent questions:** LeetCode 859 – [Buddy Strings](https://leetcode.com/problems/buddy-strings/) · LeetCode 1790 – [Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)

---

## 6. Repeated Substring Pattern — `06_repeated_substring_pattern.py`

**Brute force:** For every block size that divides n, check `s[i] == s[i - size]` for all i.
Time **O(n · d(n))** ≈ **O(n√n)** worst · Space **O(1)**

**Optimal:** KMP's LPS table. Block = `n − lps[n−1]`; True if `lps[n−1] > 0` and the block divides n.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 459 – [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) · GFG – "Find if a string can be formed by repeating a substring"
