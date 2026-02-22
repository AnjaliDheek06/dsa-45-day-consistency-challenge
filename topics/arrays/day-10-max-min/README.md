# Day 07 — Min and Max in Array

## Problem

Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

## Approach (Single Traversal)

Initialize two variables mini and maxi with the first element of the array.
Traverse the array starting from index 1.
If current element is smaller than mini, update mini.
If current element is greater than maxi, update maxi.
Return both values in a vector.

## Complexity

Time Complexity:
Single traversal of the array → O(n)

Space Complexity:
No extra space used (only two variables) → O(1)

## Key Learning

Avoided sorting (which would take O(n log n)).
Used single-pass traversal to optimize performance.
Maintained running minimum and maximum efficiently.
Learned importance of initializing with first element to avoid incorrect comparisons.
