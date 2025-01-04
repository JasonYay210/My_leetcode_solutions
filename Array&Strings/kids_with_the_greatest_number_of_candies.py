from typing import List


class Solution:

    # Question: 1431

    # 0ms Beats 100%
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        return [i + extraCandies >= M for i in candies]