from typing import List


class Solution:
    # Question: 238

    # 3ms Beats 93.48%
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            if merged[-1][1] >= i[0] and merged[-1][1] <= i[1]:
                merged[-1][1] = i[1]
        return merged

