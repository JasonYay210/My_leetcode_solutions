from typing import List


class Solution:
    # Question: 1

    # 0ms Beats 100%
    # Time Complexity: O(n) m being the defaultdicts
    # Space Complexity: O(n)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}


        for i in range(len(nums)):
            mydict[nums[i]] = i

        for i in range(len(nums)):
            end = target - nums[i]
            if end in mydict and mydict[end] != i:
                return [i,mydict[end]]