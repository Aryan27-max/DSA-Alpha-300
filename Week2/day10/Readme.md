# Day 10 - Two Pointers

Today I practised the two-pointer approach in Python. The main idea is to use pointers to go through a list and modify it without creating another list.

## 1. Remove Duplicates from Sorted Array

**Approach:** Since the array is already sorted, duplicates appear next to each other. I use a `read` pointer to check each element and a `write` pointer to keep track of where the next unique element should go.

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## 2. Remove Duplicates from Sorted Array II

**Approach:** Here, each number can appear at most twice. I compare the current element with the element two positions behind the write pointer and keep it only if it doesn't create a third occurrence.

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## 3. Remove Element

**Approach:** I go through the list and copy only the elements that are not equal to the given value. The write pointer tracks the position of the next element to keep.

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## 4. Move Zeroes

**Approach:** First, I move all non-zero elements to the front while keeping their order. Then, I fill the remaining positions with zeroes.

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## What I Learned

The read pointer checks elements, while the write pointer decides where useful elements should go. This helps solve array problems efficiently without using extra data structures or shortcut libraries.
