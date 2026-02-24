from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        
        for i in range(n):
            xor ^= nums[i]
            xor ^= i
            
        return xor ^ n