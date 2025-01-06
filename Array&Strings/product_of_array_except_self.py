from typing import List


class Solution:
    # Question: 238

    # 21ms Beats 71.05%
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1] * len(nums)

        prefix=1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
