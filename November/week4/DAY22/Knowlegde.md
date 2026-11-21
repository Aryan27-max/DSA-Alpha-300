# Day 22 (Binary Search on the Answer)

## Week 4: Binary Search Depth + Sorting from Scratch

## Problems

| Type | Problem | Main Concept |
|---|---|---|
| **Primary** | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Try Every Number → BS on Answer (is mid * mid <= x?) |
| **Variant 1** | [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/) | Subtract Row by Row → BS on k (k(k+1)/2 <= n) |
| **Variant 2** | [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | BS on Answer + Greedy Feasibility Check (Dec preview) |

## Learning Objectives

- Binary search on a RANGE OF ANSWERS, not on an array.
- Write a feasibility check: "is this answer good enough?"
- Find the LAST answer that works (sqrt, coins) and the FIRST answer that works (shipping).
- Pick correct lo and hi bounds for the answer range.
- Avoid math.sqrt / math.isqrt by building it yourself.

## Key Takeaway

If you can answer "does value v work?" with a yes / no, and the answers look like T T T T F F F (or F F F T T T), you can binary search over v directly - even when there is no array at all.


## Core Concept 

sqrt(x) rounded down = the biggest number r where r * r <= x 

```
x = 8
r:          0  1  2  3  4  5  ...
r*r <= 8?   T  T  T  F  F  F
                  ↑ last T = 2 ✓
```

the answers are T T T F F F → monotonic → binary search over r from 0 to x 
we dont search inside an array - we search inside the RANGE of possible answers 
thats why its called "binary search on answer" 

at mid - 
- mid * mid <= x → mid works, but maybe something bigger works too → save it, lo = mid + 1 
- mid * mid > x → too big → hi = mid - 1 

rule for today - no math.isqrt(), no math.sqrt(), pure BS 

## Primary - Question LC 69. Sqrt(x)

LC Question - Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

Brute Force solution - Try every number 

```
class Solution:
    def mySqrt(self, x: int) -> int:
        r = 0

        # Keep going while the next number still fits.
        while (r + 1) * (r + 1) <= x:
            r += 1

        return r
```

Time Complexity = O(√x)
Space Complexity = O(1)

### to tackle this we binary search on the answer 

range of answers = 0 .. x 
check = mid * mid <= x 
we want the LAST mid where the check is True → keep track of it in ans 

Optimal solution - BS on answer 
```
class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        ans = 0

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if mid * mid <= x:
                # mid works - remember it, try bigger.
                ans = mid
                lo = mid + 1
            else:
                # Too big - try smaller.
                hi = mid - 1

        return ans
```

Time Complexity - O(log x)
Space Complexity - O(1)

## Variant 1 (Arranging Coins)- Question LC 441. Arranging Coins

LC Question - You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

## Core Concept 

k full rows need 1 + 2 + ... + k = k(k+1)/2 coins 
answer = biggest k where k(k+1)/2 <= n 

```
n = 8
k:              1  2  3  4
k(k+1)/2:       1  3  6  10
<= 8?           T  T  T  F   → last T = 3 ✓
```

exactly the same shape as sqrt - just a different check 

Brute force - Build row by row 
```
class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1

        # Keep placing full rows while we have enough coins.
        while n >= row:
            n -= row
            row += 1

        return row - 1
```

Time Complexity - O(√n)
Space Complexity - O(1)

Optimal Solution - BS on k 
```
class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo = 0
        hi = n
        ans = 0

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            coins_needed = mid * (mid + 1) // 2

            if coins_needed <= n:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
```

Time Complexity - O(log n)
Space Complexity - O(1)

## Variant 2 (Ship Packages)- Question LC 1011. Capacity To Ship Packages Within D Days

LC Question - A conveyor belt has packages that must be shipped from one port to another within days days. The ith package has weight weights[i]. Each day, we load the ship with packages in the order given by weights. We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages being shipped within days days.

## Core Concept 

answer = ship capacity 
- smallest possible = heaviest package (else that package never fits) 
- biggest needed = sum of all weights (ship everything in 1 day) 

check(capacity) - can we ship everything in <= days days? 
greedy - keep loading in order, when the next one doesnt fit, start a new day 

```
weights = [1..10], days = 5
capacity:   10  11  ...  14  15  16 ...
works?       F   F  ...   F   T   T     → first T = 15 ✓
```

bigger ship → fewer days needed → F F F T T T → find the FIRST T (like day 19) 

this "BS on answer + feasibility check" pattern comes back a lot in december 

Brute force - Try every capacity from max to sum 
```
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(capacity):
            days_needed = 1
            load = 0
            for w in weights:
                if load + w > capacity:
                    # Start a new day.
                    days_needed += 1
                    load = 0
                load += w
            return days_needed <= days

        heaviest = 0
        total = 0
        for w in weights:
            if w > heaviest:
                heaviest = w
            total += w

        for capacity in range(heaviest, total + 1):
            if can_ship(capacity):
                return capacity
        return total
```

Time Complexity - O(n * (sum - max)) (TLE)
Space Complexity - O(1)

Optimal Solution - BS on capacity + greedy check 
```
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(capacity):
            days_needed = 1
            load = 0
            for w in weights:
                if load + w > capacity:
                    days_needed += 1
                    load = 0
                load += w
            return days_needed <= days

        lo = 0
        hi = 0
        for w in weights:
            if w > lo:
                lo = w      # heaviest package
            hi += w         # all packages in one day

        # First capacity that works.
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can_ship(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
```

Time Complexity - O(n * log(sum))
Space Complexity - O(1)
