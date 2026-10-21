# Day 1 · Two Sum
**Topic:** Hashmap lookup

Two Sum is the "remember what you've seen in a dict" pattern. Once this clicks, a huge number of problems get easier. The variants show the other side of the coin: when the array is **sorted**, you don't even need a dict, two pointers do the job.

> Rule reminder: no `collections`, no `sorted()` / `.sort()` in October. Files that need sorting have their own hand-written `merge_sort`.

---

## 1. Two Sum (PRIMARY) — `01_two_sum.py`
Find two indexes whose values add up to `target`.

**Brute force:** Try every pair with two loops. If they add up, return them.
Time **O(n²)** · Space **O(1)**

**Optimal:** Walk once. For each number, the partner you need is `target - num`. Keep a dict of `number -> index` for everything you've passed. If the partner is already in the dict, you're done.
Time **O(n)** · Space **O(n)**

**Equivalent questions:** LeetCode 1 – [Two Sum](https://leetcode.com/problems/two-sum/) · GFG – "Key Pair" (Two Sum, yes/no version)

---

## 2. Two Sum II – Input Array Is Sorted — `02_two_sum_ii_sorted.py`
Same thing, but the array is sorted and the answer is 1-indexed.

**Brute force:** Check every pair.
Time **O(n²)** · Space **O(1)**

**Optimal:** One pointer at each end. Sum too small → move left forward. Sum too big → move right back.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** LeetCode 167 – [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · GFG – "Pair with given sum in a sorted array"

---

## 3. 3Sum — `03_three_sum.py`
All unique triplets that sum to 0.

**Brute force:** Three loops over every triplet, throw results in a set to remove repeats.
Time **O(n³)** · Space **O(k)** for the answers

**Optimal:** Sort (our own merge sort). Fix `nums[i]`, then run two pointers on the rest looking for `-nums[i]`. Skip equal neighbours to avoid duplicates.
Time **O(n²)** · Space **O(n)** (merge sort's extra list)

**Equivalent questions:** LeetCode 15 – [3Sum](https://leetcode.com/problems/3sum/) · GFG – "Find triplets with zero sum"

---

## 4. 3Sum Closest — `04_three_sum_closest.py`
Return the triplet sum that is closest to `target`.

**Brute force:** Check every triplet, keep the one with the smallest `|sum - target|`.
Time **O(n³)** · Space **O(1)**

**Optimal:** Sort, fix one number, two pointers. Every sum you see, compare it to your best so far.
Time **O(n²)** · Space **O(n)** (merge sort)

**Equivalent questions:** LeetCode 16 – [3Sum Closest](https://leetcode.com/problems/3sum-closest/) · GFG – "3 Sum Closest"

---

## 5. 4Sum — `05_four_sum.py`
All unique quadruplets that sum to `target`.

**Brute force:** Four loops. Very slow.
Time **O(n⁴)** · Space **O(k)**

**Optimal:** Sort, fix two numbers with two loops, then two pointers for the last pair. Skip duplicates at every level.
Time **O(n³)** · Space **O(n)** (merge sort)

**Equivalent questions:** LeetCode 18 – [4Sum](https://leetcode.com/problems/4sum/) · GFG – "Find All Four Sum Numbers"

---

## 6. Two Sum Less Than K — `06_two_sum_less_than_k.py`
Biggest pair sum that is strictly less than `k`, or -1.

**Brute force:** Every pair, keep the biggest one under `k`.
Time **O(n²)** · Space **O(1)**

**Optimal:** Sort, two pointers. Sum < k → it's a candidate, save it and move left up. Sum ≥ k → move right down.
Time **O(n log n)** · Space **O(n)** (merge sort)

**Equivalent questions:** LeetCode 1099 – [Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/) (Premium) · GFG – "Count pairs with sum less than target" (similar idea)

---

## 7. Pair with given sum in sorted array (GFG) — `07_pair_with_given_sum_sorted.py`
Count all pairs in a sorted array (with duplicates) that add up to `target`.

**Brute force:** Check every pair and count.
Time **O(n²)** · Space **O(1)**

**Optimal:** Two pointers. When you hit a match, count copies of the left value and copies of the right value and multiply. If both values are the same, the whole block pairs with itself: `cnt * (cnt-1) / 2`.
Time **O(n)** · Space **O(1)**

**Equivalent questions:** GFG – "Pair with given sum in a sorted array" · LeetCode 167 (closest LeetCode cousin)
