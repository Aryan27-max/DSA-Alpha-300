# Day 1 (Reccursion)

## Week 1: Recursion & Dynamic Programming

## Problems

| Type | Problem | Main Concept |
|---|---|---|
| **Primary** | [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Basic Recursion |
| **Variant 1** | [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | Recursion + Dictionary Memoization |
| **Variant 2** | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Recursion → Bottom-up Dynamic Programming |

## Learning Objectives

- Understand the fundamentals of recursion.
- Identify base cases and recursive relationships.
- Apply dictionary-based memoization to avoid repeated calculations.
- Convert recursive solutions into iterative, bottom-up DP solutions.
- Analyze time and space complexity.

## Key Takeaway

Start with simple recursion, optimize using memoization, and then transition to bottom-up dynamic programming to improve efficiency.


## Core Concept 

the core concept of recursion revolves around the fact that 
a function calls the sub functions again again iteratively 
eg F(5) you need F(4) and F(3) and for those you need more dub functions 

the recursive function needs 2 things - 
Base case - when to stop 
recursive case - how to break the problem into smaller chunks 

## Primary - Question LC 509. Fibonacci Number

Brute Brute Force solution - 

```
Python - 

def count_down(n):
    # Stop when we reach zero.
    if n == 0:
        return

    print(n)

    # Call the same function with a smaller number.
    count_down(n - 1)
```

Time Complexity = O(2^n)
Space Complexity =  O(n)

### to tackle this we use dicts 

Now what is an Dictionary (dict) - 

a dictionary stores values as key-value pairs 

```
memo = {}

memo[5] = 8
memo[6] = 10 

print(memo[5]) #8
```

think of it as a dictionary 
in Recursion we use we use dictionary to remember recursion answers we have already calculated 
this is called Memoization 
instead of calculating Fib(5) again we check if it is already stored

Optimal solution - Iterative DP 
```
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # Keep track of the previous two numbers.
        a = 0
        b = 1

        for i in range(2, n + 1):
            current = a + b

            # Move forward in the sequence.
            a = b
            b = current

        return b
```

the main core is that when taking out lets say F(5) the system just have to 
remember F(4) and F(3) instead of all

Time Complexity - O(n)
Space Complexity - O(1)

## Variant 1 (Nth Tribonacci number)- Question LC 1137. N-th Tribonacci Number

## Core Concept 

Fibonacci Uses 2 prev numbers 
Tribonacci uuses 3 prev nums 
T(0) = 0
T(1) = 1
T(2) = 1

T(n) = T(n-1) + T(n-2) + T(n-3)

sequence - 0, 1, 1, 2, 4, 7, 13, 24, ...

Brute force - calculate each number one by one - 
```
class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0 
        
        if n <=2:
            return 1

        return(
            self.tribonacci(n-1)
            +self.tribonacci(n-2)
            +self.tribonacci(n-3)
        )
```

Time Complexity - O(n)
Space Complexity - O(n)

## Variant 2 (Climbing Stairs)- Question LC 70. Climbing Stairs

LC Question - You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Core Concept - 
Concept
You can climb either:
- 1 step
- 2 steps
Suppose you're trying to reach stair n.

Your last move must have come from either:
- Stair n-1, using a 1-step jump
- Stair n-2, using a 2-step jump

Therefore:
ways(n)=ways(n-1)+ways(n-2)

This is basically Fibonacci with different starting values.

brute Force - Recurssion (go through each and every step)
```
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        return (
            self.climbStairs(n-1)
            +self.climbStairs(n-2)
        )
```

Optimal Solution - (bottom up DP) - Remember the steps before 
ex - for F(5) = F(4)+F(3)
```
class Solution:
    def climbStairs(self, n: int) -> int:

        if n<= 2:
            return n

        one_step_before  = 1
        two_step_before  = 2

        for stairs in range(3,n+1):
            current = one_step_before + two_step_before

            one_step_before=two_step_before
            two_step_before = current
        return two_step_before
```
