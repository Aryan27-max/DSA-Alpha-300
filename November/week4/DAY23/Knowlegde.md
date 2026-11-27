# Day 23 (BS Variant + Newton's Method)

## Week 4: Binary Search Depth + Sorting from Scratch

## Problems

| Type | Problem | Main Concept |
|---|---|---|
| **Primary** | [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) | BS on Answer vs Newton's Method |
| **Variant 1** | [633. Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/) | Own isqrt (BS) + Two Pointers on Squares |
| **Variant 2** | [754. Reach a Number](https://leetcode.com/problems/reach-a-number/) | Math Observation + BS on Steps |

## Learning Objectives

- Check a perfect square with BS (exact match instead of "last that fits").
- Implement Newton's method with integers and compare it with BS.
- Build your own isqrt and reuse it inside other problems.
- Use two pointers on a range of numbers (not an array).
- Turn a puzzle into a math condition, then BS on it.

## Key Takeaway

Same problem, two fast ways: binary search halves the range every step (log n steps), Newton's method jumps closer using r = (r + n / r) / 2 and gets there in even fewer steps. Both need zero math library.


## Core Concept 

perfect square = some integer r where r * r == num exactly 
eg 16 = 4 * 4 ✓, 14 ✗ 

way 1 - BS (day 22) 
search r in 1..num, but now we look for EXACT mid * mid == num 
- equal → True 
- smaller → lo = mid + 1 
- bigger → hi = mid - 1 
loop ends without finding → False 

way 2 - Newton's method 
start with a guess r (eg r = num), then improve it - 
r = (r + num // r) // 2 
if r is too big, num // r is too small, their average is closer to the real root 

```
num = 16
r = 16 → (16 + 1) // 2  = 8
r = 8  → (8 + 2) // 2   = 5
r = 5  → (5 + 3) // 2   = 4
r = 4  → 4 * 4 = 16, stop → perfect square ✓
```

rule for today - no math.isqrt(), BS or Newton 

## Primary - Question LC 367. Valid Perfect Square

LC Question - Given a positive integer num, return true if num is a perfect square or false otherwise.
You must not use any built-in library function, such as sqrt.

Brute Force solution - Try every number 

```
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False
```

Time Complexity = O(√n)
Space Complexity = O(1)

Optimal solution 1 - Binary search 
```
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
```

Time Complexity - O(log n)
Space Complexity - O(1)

Optimal solution 2 - Newton's method 
```
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num

        # Keep improving the guess while it is too big.
        while r * r > num:
            r = (r + num // r) // 2

        return r * r == num
```

Time Complexity - O(log n) (in practice fewer steps than BS)
Space Complexity - O(1)

### BS vs Newton 

BS → cuts the range in half every step, very predictable, easy to write on paper 
Newton → error shrinks super fast near the answer (number of correct digits roughly doubles) 
for an interview - BS is safer to write, Newton is a nice "follow up" 

## Variant 1 (Sum of Square Numbers)- Question LC 633. Sum of Square Numbers

LC Question - Given a non-negative integer c, decide whether there're two integers a and b such that a² + b² = c.

## Core Concept 

eg 5 = 1² + 2² ✓, 3 ✗ 

a and b are both between 0 and √c 

way 1 - for every a, check if c - a² is a perfect square (use the primary!) 

way 2 - two pointers (oct day 1 two sum on sorted, but on squares) 
a = 0 (smallest), b = isqrt(c) (biggest) 
- a² + b² == c → found 
- too small → a += 1 (make it bigger) 
- too big → b -= 1 (make it smaller) 

isqrt(c) we build ourselves with the day 22 BS 

Brute force - For every a, BS check if c - a² is a square 
```
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        def is_square(num):
            lo = 0
            hi = num
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if mid * mid == num:
                    return True
                elif mid * mid < num:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False

        a = 0
        while a * a <= c:
            if is_square(c - a * a):
                return True
            a += 1

        return False
```

Time Complexity - O(√c * log c)
Space Complexity - O(1)

Optimal Solution - Own isqrt + two pointers 
```
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        def isqrt(x):
            lo = 0
            hi = x
            ans = 0
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if mid * mid <= x:
                    ans = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans

        a = 0
        b = isqrt(c)

        while a <= b:
            total = a * a + b * b
            if total == c:
                return True
            elif total < c:
                a += 1
            else:
                b -= 1

        return False
```

Time Complexity - O(√c)
Space Complexity - O(1)

## Variant 2 (Reach a Number)- Question LC 754. Reach a Number

LC Question - You are standing at position 0 on an infinite number line. There is a destination at position target.
You can make some number of moves numMoves so that on each move i (starting from i = 1 to i = numMoves), you take i steps in either direction. Return the minimum number of moves required to reach the destination.

## Core Concept 

left or right doesnt matter by symmetry → target = abs(target) 

if we go right every time, after k moves we are at sum = 1 + 2 + ... + k 
flipping move i from right to left changes the sum by 2i (an EVEN number) 

so we need - 
1. sum >= target (we went far enough) 
2. (sum - target) is even (we can fix the extra by flipping some moves) 

```
target = 2
k=1 sum=1  → too small
k=2 sum=3  → diff 1 odd ✗
k=3 sum=6  → diff 4 even ✓   (-1 +2... → 1 - 2 + 3 = 2) → answer 3
```

way 1 - just keep adding k till both conditions are true 
way 2 - BS (like day 22 V1 arranging coins) to find the smallest k with sum >= target, then add at most 2 more moves to fix the parity 

Brute force - Keep adding moves 
```
class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = -target

        k = 0
        total = 0

        # Need to reach or pass target, with an even overshoot.
        while total < target or (total - target) % 2 != 0:
            k += 1
            total += k

        return k
```

Time Complexity - O(√target)
Space Complexity - O(1)

Optimal Solution - BS for the first k with sum >= target, then fix parity 
```
class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = -target

        # First k where 1 + 2 + ... + k >= target.
        lo = 0
        hi = target
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * (mid + 1) // 2 >= target:
                hi = mid
            else:
                lo = mid + 1

        k = lo
        total = k * (k + 1) // 2

        # At most 2 extra moves make the overshoot even.
        while (total - target) % 2 != 0:
            k += 1
            total += k

        return k
```

Time Complexity - O(log target)
Space Complexity - O(1)
