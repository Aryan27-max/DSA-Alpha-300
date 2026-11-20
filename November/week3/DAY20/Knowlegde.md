# Day 20 (BS Lower Bound — bisect_left Rebuilt)

## Week 3: Linked Lists Part 2 + Binary Search Intro

## Problems

| Type | Problem | Main Concept |
|---|---|---|
| **Primary** | [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Lower Bound: First Index where nums[i] >= target |
| **Variant 1** | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | BS + "Which Half is Sorted?" Check |
| **Variant 2** | [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Treat the Matrix as One Flattened Sorted Array |

## Learning Objectives

- Build the lower_bound function yourself (the thing bisect_left does).
- Understand why hi starts at n (the answer can be "after everything").
- Binary search a rotated array by finding the sorted half each step.
- Convert a 1D index to (row, col) with // and %.
- See that lower bound is the building block of most other BS problems.

## Key Takeaway

lower_bound(target) = first index where nums[i] >= target. If target exists, that's its index; if not, that's exactly where it would be inserted. Every other BS variant (first / last position, count, floor / ceiling) is built from this one function.


## Core Concept 

search insert position = if found return the index, else return where it SHOULD go 

```
nums = [1, 3, 5, 6]

target 5 → index 2 (found)
target 2 → index 1 (goes between 1 and 3)
target 7 → index 4 (goes after everything)
target 0 → index 0
```

all 4 cases are the same question - first index where nums[i] >= target 
```
nums     1  3  5  6
>= 2 ?   F  T  T  T   → first T = 1 ✓
>= 7 ?   F  F  F  F   → no T → answer = n = 4 ✓
```

same F F T T boundary as day 19 
thats why hi starts at len(nums) (not len - 1) - "n" is a valid answer 

rule for today - no bisect_left, build the lower bound function yourself 

## Primary - Question LC 35. Search Insert Position

LC Question - Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Brute Force solution - Linear scan for the first nums[i] >= target 

```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        # Bigger than everything.
        return len(nums)
```

Time Complexity = O(n)
Space Complexity = O(1)

### to tackle this we build our own lower_bound 

this is the template we will reuse on day 24 (first and last position) and later 

```
def lower_bound(nums, target):
    lo = 0
    hi = len(nums)        # n is a valid answer

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid      # mid could be the answer
        else:
            lo = mid + 1  # answer is after mid

    return lo
```

Optimal solution - Lower bound 
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        return lo
```

Time Complexity - O(log n)
Space Complexity - O(1)

## Variant 1 (Rotated Sorted Array)- Question LC 33. Search in Rotated Sorted Array

LC Question - There is an integer array nums sorted in ascending order (with distinct values), possibly rotated at an unknown pivot index. Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

## Core Concept 

eg [0, 1, 2, 4, 5, 6, 7] rotated → [4, 5, 6, 7, 0, 1, 2] 

the whole array is not sorted, BUT if we cut it at any mid, at least ONE half is sorted 

```
[4, 5, 6, 7, 0, 1, 2]
          mid
left half [4, 5, 6, 7] → sorted (nums[lo] <= nums[mid])
right half [7, 0, 1, 2] → not sorted
```

at each step - 
1. which half is sorted? → nums[lo] <= nums[mid] means left is sorted 
2. is the target inside that sorted half? (easy check - between its first and last value) 
   - yes → go there 
   - no → go to the other half 

Brute force - Linear scan 
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```

Time Complexity - O(n)
Space Complexity - O(1)

Optimal Solution - BS + sorted half check 
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                # Left half lo..mid is sorted.
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # Right half mid..hi is sorted.
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
```

Time Complexity - O(log n)
Space Complexity - O(1)

## Variant 2 (Search a 2D Matrix)- Question LC 74. Search a 2D Matrix

LC Question - You are given an m x n integer matrix with the following two properties: each row is sorted in non-decreasing order, and the first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise. You must write a solution in O(log(m * n)) time complexity.

## Core Concept 

because every row starts after the previous row ends, if we read it row by row its ONE sorted array 

```
[[1,  3,  5,  7],
 [10, 11, 16, 20],
 [23, 30, 34, 60]]

flattened: 1 3 5 7 10 11 16 20 23 30 34 60
index:     0 1 2 3  4  5  6  7  8  9 10 11
```

we dont actually build the flat array - we just convert index → (row, col) 
row = index // cols 
col = index % cols 

eg index 6 with 4 cols → row 6 // 4 = 1, col 6 % 4 = 2 → matrix[1][2] = 16 ✓ 

then its just day 18 binary search on 0 .. m*n - 1 

Brute force - Check every cell 
```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for value in row:
                if value == target:
                    return True
        return False
```

Time Complexity - O(m * n)
Space Complexity - O(1)

### Better - binary search inside each row 
```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            lo = 0
            hi = len(row) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
```

Time Complexity - O(m log n)
Space Complexity - O(1)

Optimal Solution - One binary search on the flattened index 
```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        lo = 0
        hi = rows * cols - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # 1D index -> 2D position.
            value = matrix[mid // cols][mid % cols]

            if value == target:
                return True
            elif value < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
```

Time Complexity - O(log(m * n))
Space Complexity - O(1)
