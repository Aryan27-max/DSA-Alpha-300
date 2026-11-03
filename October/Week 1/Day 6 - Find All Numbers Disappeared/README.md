# Day 6 · Find All Numbers Disappeared in an Array
**Topic:** In-place marking (O(1) space trick)

When the values are in the range 1..n, every value has a natural "home" index (`v - 1`). That means the array can act as its own hashmap: flip a sign to say "seen", or swap numbers into their homes (cyclic sort). Interviewers love this because it turns O(n) space into O(1).

> No `set(range(1, n+1)) - set(nums)`. The set versions below are only the brute force to compare against.

---

## 1. Find All Numbers Disappeared in an Array (PRIMARY) — `01_find_disappeared_numbers.py`
Values are 1..n with some duplicates; return the missing ones.

**Brute force:** Put everything in a set, check 1..n.
Time **O(n)** · Space **O(n)**

**Optimal:** For every value `v`, make `nums[v-1]` negative. Any index that's still positive means `index + 1` is missing.
Time **O(n)** · Space **O(1)** (output not counted)

**Equivalent questions:** LeetCode 448 – [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) · GFG – "Find missing elements of a range"

---

## 2. Missing Number — `02_missing_number.py`
0..n with exactly one missing.

**Brute force:** Set of values, check 0..n.
Time **O(n)** · Space **O(n)**

**Optimal:** `n(n+1)/2 − sum(nums)` (Day 3 did the XOR version).
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 268 – [Missing Number](https://leetcode.com/problems/missing-number/) · GFG – "Missing number in array"

---

## 3. Find All Duplicates in an Array — `03_find_all_duplicates.py`
Values 1..n, each once or twice; return the twice ones.

**Brute force:** Set; when you see something already in it, it's a duplicate.
Time **O(n)** · Space **O(n)**

**Optimal:** Cyclic sort — swap every value to index `v-1`. Afterwards, anything not at its home is a duplicate. (Day 2's file shows the negative-marking way.)
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 442 – [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) · GFG – "Find duplicates in an array"

---

## 4. First Missing Positive — `04_first_missing_positive.py`
Smallest positive integer not in an unsorted list. O(n) time, O(1) space.

**Brute force:** Put everything in a set, count up from 1 until something is missing.
Time **O(n)** · Space **O(n)**

**Optimal:** Answer is in 1..n+1. Cyclic sort only values in 1..n into their homes, ignore the rest. First index `i` with `nums[i] != i+1` → answer `i+1`. Otherwise `n+1`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 41 – [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) · GFG – "Smallest Positive missing number"

---

## 5. Set Mismatch — `05_set_mismatch.py`
One number in 1..n got duplicated and replaced another. Return `[dup, missing]`.

**Brute force:** Count with a dict, then check 1..n for count 2 and count 0.
Time **O(n)** · Space **O(n)**

**Optimal:** Negative marking. If the home is already negative → that's the duplicate. The one home that stays positive → that's the missing number.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 645 – [Set Mismatch](https://leetcode.com/problems/set-mismatch/) · GFG – "Find Missing And Repeating"

---

## 6. Missing number in array (GFG) — `06_missing_number_gfg.py`
n−1 numbers from 1..n, one missing.

**Brute force:** Sum formula `n(n+1)/2 − total` (fine in Python, can overflow in C++/Java).
Time **O(n)** · Space **O(1)**

**Optimal:** XOR all of 1..n with all array values; the leftover is the answer. No overflow risk.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** GFG – "Missing number in array" · LeetCode 268 – [Missing Number](https://leetcode.com/problems/missing-number/) (0..n version)
