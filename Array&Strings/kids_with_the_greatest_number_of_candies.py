class Solution:

    #

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        return [i + extraCandies >= M for i in candies]