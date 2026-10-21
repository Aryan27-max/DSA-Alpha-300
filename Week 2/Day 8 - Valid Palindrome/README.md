# Day 8 · Valid Palindrome
**Topic:** Two pointers from ends

The simplest two-pointer pattern: one finger at the start, one at the end, walk them toward each other. Today's twist is handling junk characters *while* you walk instead of cleaning the string first.

> No `s == s[::-1]` and no `''.join(c for c in s if c.isalnum()).lower()` one-liner.

---

## 1. Valid Palindrome (PRIMARY) — `01_valid_palindrome.py`
Ignore non-alphanumerics and case; does it read the same both ways?

**Brute force:** Build a cleaned, lowercased list first, then compare from both ends.
Time **O(n)** · Space **O(n)**

**Optimal:** Two pointers on the original string. Skip junk on either side, compare lowercased characters, move inward.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 125 – [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) · GFG – "Palindrome String"

---

## 2. Valid Palindrome II — `02_valid_palindrome_ii.py`
Can it become a palindrome by deleting at most one character?

**Brute force:** Try deleting each character and check the rest.
Time **O(n²)** · Space **O(n)**

**Optimal:** Normal two-pointer walk. At the first mismatch, check if skipping the left char **or** the right char leaves a palindrome.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 680 – [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) · GFG – "Check if a string can become palindrome by removing at most one character"

---

## 3. Palindrome Linked List — `03_palindrome_linked_list.py`

**Brute force:** Copy the values into a list, two-pointer check.
Time **O(n)** · Space **O(n)**

**Optimal:** Slow/fast pointers to find the middle, reverse the second half, compare the halves, reverse it back.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 234 – [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) · GFG – "Check if Linked List is Palindrome"

---

## 4. Palindromic Substrings — `04_palindromic_substrings.py`
Count all palindromic substrings.

**Brute force:** Check every substring with two pointers.
Time **O(n³)** · Space **O(1)**

**Optimal:** Expand around each of the 2n−1 centers (each char and each gap), counting every successful step outward.
Time **O(n²)** · Space **O(1)**

**Equivalent questions:** LeetCode 647 – [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) · LeetCode 5 – [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (same expand trick) · GFG – "Count All Palindromic Substrings"

---

## 5. Reverse Only Letters — `05_reverse_only_letters.py`
Reverse letters; non-letters stay put.

**Brute force:** Collect letters in a list, then refill them by popping from the end.
Time **O(n)** · Space **O(n)** extra

**Optimal:** Two pointers that skip non-letters and swap letters in a char list.
Time **O(n)** · Space **O(n)** (only the char list, which Python needs since strings can't be changed)

**Equivalent questions:** LeetCode 917 – [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/) · GFG – "Reverse a string without affecting special characters"

---

## 6. Palindrome Number — `06_palindrome_number.py`
Is an integer a palindrome, without converting to a string?

**Brute force:** Convert to a string, two-pointer check.
Time **O(d)** · Space **O(d)** (d = number of digits)

**Optimal:** Reverse only the last half of the digits with `% 10` and `// 10`, then compare with the first half.
Time **O(d)** · Space **O(1)**

**Equivalent questions:** LeetCode 9 – [Palindrome Number](https://leetcode.com/problems/palindrome-number/) · GFG – "Palindrome Number"
