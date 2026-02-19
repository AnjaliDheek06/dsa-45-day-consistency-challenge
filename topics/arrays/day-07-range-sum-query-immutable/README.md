# Day 07 — Range Sum Query-Immutable

## Problem
Given an integer array, calculate the sum of elements between indices left and right (inclusive).
The array does not change (immutable).


## Approach
Used Prefix Sum array
Precomputed cumulative sums in constructor
Each query answered in O(1) time using:  prefix[right] - prefix[left - 1]
Special handling when left == 0


## Complexity
Preprocessing: O(n)
Query: O(1)
Space: O(n)



## Key Learning
Prefix sum pattern
Turning repeated O(n) queries into O(1)
