from typing import Counter, List


class Solution:


    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i in counter:
            if counter[i] > len(nums) / 2:
                return i
