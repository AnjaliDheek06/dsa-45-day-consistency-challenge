# Day 12 — Missing Number

## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number that is missing from the array.

## Approach (XOR Method — Single Traversal)

Initialize a variable `xor` with 0.

Store the size of the array in variable `n`.

Traverse the array from index 0 to n-1.

For each index:
- XOR the array element with `xor`.
- XOR the index value with `xor`.

After the loop, XOR the result with `n`.

Return the final value.

This works because identical numbers cancel out using XOR, leaving only the missing number.

## Complexity

Time Complexity:  
Single traversal of the array → O(n)

Space Complexity:  
No extra space used (only one variable) → O(1)

## Key Learning

Used XOR properties to cancel out duplicate values.
Avoided sorting and extra space.
Learned that XOR of same numbers becomes zero.
Understood how mathematical properties can optimize array problems.
Achieved optimal time and space complexity.