from typing import Counter, List


class Solution:
    # Question: 169

    # 0ms Beats 100%
    # Time Complexity: O(n + m) m being set_jewels
    # Space Complexity: O(m)

    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i in counter:
            if counter[i] > len(nums) / 2:
                return i
