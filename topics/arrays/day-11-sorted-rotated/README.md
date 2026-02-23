# Day 11— Check if Array is Sorted and Rotated 

## Problem
Given an array `nums`, check whether it was originally sorted in non-decreasing order and then rotated some number of times.

Return `true` if it is, otherwise return `false`.


## Approach

 Traverse the array from index 1 to n-1.

Count how many times the sorted order breaks:
   If `nums[i-1] > nums[i]`, increment `count`.

 Since rotation connects the last element to the first,
   check if `nums[n-1] > nums[0]`.
   If true, increment `count`.

If `count` is less than or equal to 1,
   the array is either:
   - Fully sorted
   - Sorted and rotated once

Otherwise, it is not valid.


## Complexity Analysis

- Time Complexity: **O(n)**
  - Single traversal of the array

- Space Complexity: **O(1)**
  - Only constant variables used


## Key Learning

- Learned how to detect sorted order violations.
- Understood how rotation affects array boundaries.
- Practiced counting inversion points.
- Strengthened reasoning about edge cases in array problems.

## Pattern Used

Linear Traversal + Inversion Counting