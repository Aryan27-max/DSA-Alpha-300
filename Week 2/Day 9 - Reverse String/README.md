# Day 9 · Reverse String
**Topic:** In-place swap

Swap the two ends, move inward, repeat. This tiny loop is the building block for half of today's problems — reverse a chunk, reverse only some characters, reverse each word, or reverse everything twice. The primary also has a recursive version as a warm-up for November.

> No `s.reverse()`, `reversed(s)` or `s[::-1]`. The lesson IS the loop.

---

## 1. Reverse String (PRIMARY) — `01_reverse_string.py`
Reverse a list of chars in place.

**Brute force:** Copy into a new list from the back, then copy it over the original.
Time **O(n)** · Space **O(n)**

**Optimal:** Two pointers from the ends, swap, move inward.
Time **O(n)** · Space **O(1)**
*(Recursive version: same time, O(n) stack space.)*

**Equivalent questions:** LeetCode 344 – [Reverse String](https://leetcode.com/problems/reverse-string/) · GFG – "Reverse a String"

---

## 2. Reverse String II — `02_reverse_string_ii.py`
Reverse the first k chars of every 2k block.

**Brute force:** Build the answer chunk by chunk into a new list, reading the first k backwards.
Time **O(n)** · Space **O(n)**

**Optimal:** Jump through the list in steps of 2k and run the swap loop on `[start, min(start+k-1, n-1)]`.
Time **O(n)** · Space **O(n)** for the char list (Python strings can't be changed)

**Equivalent questions:** LeetCode 541 – [Reverse String II](https://leetcode.com/problems/reverse-string-ii/) · GFG – "Reverse every k characters"

---

## 3. Reverse Vowels of a String — `03_reverse_vowels.py`

**Brute force:** Collect vowels, then refill them by popping from the end.
Time **O(n)** · Space **O(n)**

**Optimal:** Two pointers that skip non-vowels (checked with a set) and swap vowel pairs.
Time **O(n)** · Space **O(n)** for the char list

**Equivalent questions:** LeetCode 345 – [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) · GFG – "Reverse vowels in a given string"

---

## 4. Reverse Words in a String III — `04_reverse_words_iii.py`
Reverse letters inside each word, keep word order.

**Brute force:** Split, reverse each word into a new string, join.
Time **O(n)** · Space **O(n)**

**Optimal:** One pass over a char list; whenever a word ends, swap-reverse just that word.
Time **O(n)** · Space **O(n)** for the char list

**Equivalent questions:** LeetCode 557 – [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) · GFG – "Reverse each word in a given string"

---

## 5. Reverse Prefix of Word — `05_reverse_prefix_of_word.py`
Reverse up to and including the first `ch`.

**Brute force:** Build a new string: the prefix read backwards plus the rest.
Time **O(n)** · Space **O(n)**

**Optimal:** Find the first `ch`, then swap-reverse `[0, i]`.
Time **O(n)** · Space **O(n)** for the char list

**Equivalent questions:** LeetCode 2000 – [Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/)

---

## 6. Reverse Words in a String — `06_reverse_words_in_a_string.py`
Reverse word order and clean up extra spaces.

**Brute force:** `split()`, swap words with two pointers, `join`.
Time **O(n)** · Space **O(n)**

**Optimal:** Clean spaces into a char list, reverse the whole list, then reverse each word back. All three steps are the same swap loop.
Time **O(n)** · Space **O(n)** (O(1) extra in languages with mutable strings)

**Equivalent questions:** LeetCode 151 – [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) · GFG – "Reverse words in a given string"
