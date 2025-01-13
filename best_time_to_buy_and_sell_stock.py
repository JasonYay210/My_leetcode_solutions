from typing import List


class Solution:
    
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