from typing import List


class Solution:
    # Question: 121

    # 24ms Beats 92.18%
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        ans = 0
        for price in prices:
            if min_price > price:
                min_price = price
            profit = price - min_price
            if profit > ans:
                ans = profit
        return ans