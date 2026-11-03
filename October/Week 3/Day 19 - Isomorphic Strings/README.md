# Day 19 · Isomorphic Strings
**Topic:** Bijective hashmap (two dicts)

A one-way dict only checks that each letter always maps to the same thing. It does **not** stop two different letters from mapping to the same target ("badc" → "baba": b→b and d→b). You need a second dict going the other way. Together they make the mapping one-to-one. The variants apply that to words, to many candidates, and to "what stays the same after allowed swaps".

> No `len(set(zip(s,t))) == len(set(s)) == len(set(t))`. Build both dicts explicitly — the primary file includes the buggy one-way version so you can see it fail.

---

## 1. Isomorphic Strings (PRIMARY) — `01_isomorphic_strings.py`

**Brute force:** For every pair of positions, `s[i]==s[j]` must equal `t[i]==t[j]`.
Time **O(n²)** · Space **O(1)**

**Optimal:** Two dicts, `s→t` and `t→s`. Every pair must agree with both.
Time **O(n)** · Space **O(alphabet)**

**Why both dicts?** `s→t` alone accepts "badc"/"baba" (b→b, a→a, d→b, c→a are each consistent). `t→s` catches that `b` is claimed by both `b` and `d`.

**Equivalent questions:** LeetCode 205 – [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) · GFG – "Isomorphic Strings"

---

## 2. Word Pattern — `02_word_pattern.py`

**Brute force:** Compare every pair of positions.
Time **O(n²)** · Space **O(n)** for the word list

**Optimal:** `split()`, then two dicts (letter→word, word→letter).
Time **O(n + total chars)** · Space **O(n)**

**Equivalent questions:** LeetCode 290 – [Word Pattern](https://leetcode.com/problems/word-pattern/)

---

## 3. Find and Replace Pattern — `03_find_and_replace_pattern.py`

**Approach A:** Two-dict bijection check on every word.
Time **O(k · L)** · Space **O(L)**

**Approach B (cleaner):** Normal form — each letter becomes the order it first appeared (`"abb"` → `[0,1,1]`). Compute the pattern's once, compare.
Time **O(k · L)** · Space **O(L)**

**Equivalent questions:** LeetCode 890 – [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)

---

## 4. Buddy Strings — `04_buddy_strings.py`
(Day 17 used mismatch indexes; this version thinks of each mismatch as a mapping `x → y`.)

**Brute force:** Try every swap.
Time **O(n³)** · Space **O(n)**

**Optimal:** Collect mismatched pairs. Two pairs that mirror each other (`x→y`, `y→x`) → True. Zero pairs → True if any letter repeats.
Time **O(n)** · Space **O(alphabet)**

**Equivalent questions:** LeetCode 859 – [Buddy Strings](https://leetcode.com/problems/buddy-strings/) · LeetCode 1790 – [Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)

---

## 5. Rotate String — `05_rotate_string.py`
(Day 17 used KMP on `s + s`; this version uses index mapping `goal[i] == s[(i+k) % n]`.)

**Brute force:** Build every rotation as a new string and compare.
Time **O(n²)** · Space **O(n)**

**Index-mapping version:** Only try shifts where `s[k] == goal[0]`; check with modulo indexing.
Time **O(n²)** worst, usually much faster · Space **O(1)**
*(Guaranteed O(n): Day 17's KMP version.)*

**Equivalent questions:** LeetCode 796 – [Rotate String](https://leetcode.com/problems/rotate-string/) · GFG – "Check if strings are rotations of each other or not"

---

## 6. Groups of Special-Equivalent Strings — `06_groups_special_equivalent.py`

**Brute force:** Compare each word with a representative of every existing group.
Time **O(n² · L)** · Space **O(n)**

**Optimal:** Signature = (letter counts at even indexes, letter counts at odd indexes) as a 52-slot tuple; count distinct signatures in a set.
Time **O(n · L)** · Space **O(n)**

**Equivalent questions:** LeetCode 893 – [Groups of Special-Equivalent Strings](https://leetcode.com/problems/groups-of-special-equivalent-strings/) · LeetCode 49 – [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (same signature idea)
