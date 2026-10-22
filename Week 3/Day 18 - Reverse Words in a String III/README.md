# Day 18 · Reverse Words in a String III
**Topic:** String split + in-place reverse

Week 2's swap loop meets tokenizing: walk the characters, notice where each word starts and ends, and reverse just that slice. Combine it with "reverse the whole thing first" and you get the classic **reverse everything, then reverse the parts** trick. The variants practise walking strings by index (from the end, by ASCII code, with read/write pointers).

> No `' '.join(w[::-1] for w in s.split())`. Build a list, walk char by char, reverse each word in place with the Day 9 swap.

---

## 1. Reverse Words in a String III (PRIMARY) — `01_reverse_words_iii.py`

**Brute force:** `split`, build each reversed word in a new list, `join`.
Time **O(n)** · Space **O(n)** (several extra lists/strings)

**Optimal:** One pass over a char list; when a word ends, swap-reverse `chars[start..i-1]`.
Time **O(n)** · Space **O(n)** for the char list only (O(1) extra in languages with mutable strings)

**Equivalent questions:** LeetCode 557 – [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) · GFG – "Reverse each word in a given string"

---

## 2. Reverse Words in a String — `02_reverse_words_in_a_string.py`

**Brute force:** `split()`, read the words backwards into a new list, `join`.
Time **O(n)** · Space **O(n)**

**Optimal:** Clean spaces into a char list → reverse the whole list → reverse each word (the primary).
Time **O(n)** · Space **O(n)** (O(1) extra with mutable strings)

**Equivalent questions:** LeetCode 151 – [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) · GFG – "Reverse words in a given string"

---

## 3. Reverse Only Letters — `03_reverse_only_letters.py`

**Brute force:** Collect the letters, pop them back in reverse order.
Time **O(n)** · Space **O(n)** extra

**Optimal:** Two pointers that skip non-letters (checked by ASCII range) and swap letters.
Time **O(n)** · Space **O(n)** for the char list

**Equivalent questions:** LeetCode 917 – [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/) · GFG – "Reverse a string without affecting special characters"

---

## 4. Length of Last Word — `04_length_of_last_word.py`

**Brute force:** `split()` and measure the last word.
Time **O(n)** · Space **O(n)**

**Optimal:** From the end: skip trailing spaces, then count letters until a space.
Time **O(length of last word + trailing spaces)** · Space **O(1)**

**Equivalent questions:** LeetCode 58 – [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) · GFG – "Length of Last word"

---

## 5. To Lower Case — `05_to_lower_case.py`

**Brute force:** Look each character up in a hand-written uppercase alphabet.
Time **O(26 · n)** · Space **O(n)**

**Optimal:** ASCII arithmetic — if `65 ≤ ord(ch) ≤ 90`, `chr(ord(ch) + 32)`.
Time **O(n)** · Space **O(n)** for the output

**Equivalent questions:** LeetCode 709 – [To Lower Case](https://leetcode.com/problems/to-lower-case/) · GFG – "Convert string to lowercase"

---

## 6. String Compression — `06_string_compression.py`

**Brute force:** Build the compressed list separately, copy it back.
Time **O(n)** · Space **O(n)**

**Optimal:** Read pointer measures each run; write pointer puts down the char and its count digits (peeled with `% 10`, then flipped with the swap loop).
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 443 – [String Compression](https://leetcode.com/problems/string-compression/) · GFG – "Run Length Encoding"
