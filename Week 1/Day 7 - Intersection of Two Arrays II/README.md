# Day 7 · Intersection of Two Arrays II
**Topic:** Hashmap counting + multiset

A set answers "is it there?". A count dict (a multiset) answers "how many are there?". Today's lesson is knowing which one the problem needs: unique intersection → set, intersection with duplicates → count dict, sorted input → maybe no hashing at all, just pointers.

> No `collections.Counter` and no `&` / `-` set operators. Build the dicts and loops yourself, decrement as you walk.

---

## 1. Intersection of Two Arrays II (PRIMARY) — `01_intersection_of_two_arrays_ii.py`
Intersection keeping duplicates.

**Brute force:** For every number in `nums1`, find an unused matching copy in `nums2` (mark it used).
Time **O(n·m)** · Space **O(m)**

**Optimal:** Count the smaller list in a dict. Walk the other list; if the count is > 0, add it and decrement.
Time **O(n + m)** · Space **O(min(n, m))**

**Equivalent questions:** LeetCode 350 – [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) · GFG – "Intersection of two arrays" (with duplicates)

---

## 2. Intersection of Two Arrays — `02_intersection_of_two_arrays.py`
Intersection, unique values only.

**Brute force:** Compare every pair, check the result list before adding.
Time **O(n·m)** · Space **O(1)** extra

**Optimal:** Set from `nums1`. Walk `nums2`; if it's in the set, add it and discard it from the set.
Time **O(n + m)** · Space **O(n)**

**Equivalent questions:** LeetCode 349 – [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) · GFG – "Intersection of Two Arrays"

---

## 3. Union of Two Arrays (GFG) — `03_union_of_two_arrays.py`
All distinct elements across both arrays (and the count).

**Brute force:** Before adding each element, scan the result list.
Time **O((n+m)²)** · Space **O(n+m)**

**Optimal:** One hand-filled set plus a result list; add anything not seen yet.
Time **O(n + m)** · Space **O(n + m)**

**Equivalent questions:** GFG – "Union of Two Arrays with Duplicate Elements" · GFG – "Union of 2 Sorted Arrays" (two-pointer version)

---

## 4. Find Common Characters — `04_find_common_characters.py`
Characters common to all words, with duplicates.

**Brute force:** For each letter of the first word, check every other word has it and remove one copy from each.
Time **O(k · L²)** · Space **O(k · L)**

**Optimal:** 26-slot count list per word; keep the minimum count for each letter across all words.
Time **O(k · L)** · Space **O(1)** (26 slots)

**Equivalent questions:** LeetCode 1002 – [Find Common Characters](https://leetcode.com/problems/find-common-characters/) · GFG – "Common characters in n strings"

---

## 5. Intersection of Three Sorted Arrays — `05_intersection_of_3_sorted_arrays.py`
Numbers in all three strictly increasing arrays.

**Brute force:** Count everything in a dict, keep numbers with count 3.
Time **O(n)** · Space **O(n)**

**Optimal:** Three pointers. All equal → take it, move all. Else move the pointer(s) on the smallest value.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 1213 – [Intersection of Three Sorted Arrays](https://leetcode.com/problems/intersection-of-three-sorted-arrays/) (Premium) · GFG – "Common elements" (in three sorted arrays)

---

## 6. Find the Difference of Two Arrays — `06_find_difference_of_two_arrays.py`
Distinct numbers only in `nums1`, and distinct numbers only in `nums2`.

**Brute force:** For each number, scan the other list; avoid repeats by scanning the output.
Time **O(n·m)** · Space **O(1)** extra

**Optimal:** Build a set for each, then keep what the other set doesn't have.
Time **O(n + m)** · Space **O(n + m)**

**Equivalent questions:** LeetCode 2215 – [Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/)
