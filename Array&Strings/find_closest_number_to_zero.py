from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Question: 2239

        # 3ms Beats 85.32%
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        n = len(nums) 
        result = float("inf")
        if n == 1:
            return nums[0]

        # [2,-1,1] 
        for i in range(n):
            if abs(nums[i]) < result:
                result = abs(nums[i])
        
        if result not in nums:
            return result *-1
            
        return result
            