# Day 7 — Intersection of Two Arrays II

**Topic:** Hashmap counting + multiset

Today's main idea is understanding the difference between a **set** and a **multiset**.

A set only cares whether a value exists.

A multiset also cares about **how many times** a value exists.

For example:

```text
A = [1, 2, 2, 1]
B = [2, 2]

Set intersection      -> [2]
Multiset intersection -> [2, 2]
```

## Primary

`01_Intersection_of_Two_Arrays_II.py`

The main approach:

1. Count every value in the first array.
2. Walk through the second array.
3. If the count is greater than zero, add the value.
4. Decrease the count.

The important pattern is:

```text
freq[x] > 0
    ↓
use one occurrence
    ↓
freq[x] -= 1
```

For this practice, the frequency dictionary is built manually instead of using
`collections.Counter`.

## Variants

### 1. Intersection of Two Arrays
`02_Intersection_of_Two_Arrays.py`

Unique intersection. Duplicates are ignored.

### 2. Union with Duplicates
`03_Union_of_Two_Arrays.py`

Counts values from both arrays and keeps all occurrences.

### 3. Find Common Characters
`04_Find_Common_Characters.py`

Finds the characters that occur in every string, including duplicates.

### 4. Intersection of 3 Sorted Arrays
`05_Intersection_of_3_Sorted_Arrays.py`

Uses three pointers instead of a hashmap because the arrays are sorted.


## Complexity

For the primary problem:

- Time: **O(n + m)**
- Extra space: **O(k)**, where `k` is the number of different values stored in the dictionary.

