from typing import Counter, List


class Solution:
    # Question: 1207

    # 0ms Beats 100%
    # Time Complexity: O(n) going through to make dict
    # Space Complexity: O(u) number of unique values

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mdict = Counter(arr)
        
        if len(set(mdict.values())) != len(mdict.values()):
            return False
        return Tru