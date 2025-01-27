from typing import Counter, List


class Solution:
    # Question: 169

    # 7ms Beats 57.81%
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i in counter:
            if counter[i] > len(nums) / 2:
                return i
