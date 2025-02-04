from typing import Counter


class Solution:
    # Question: 1207

    # 0ms Beats 100%
    # Time Complexity: O(n) m being the defaultdicts
    # Space Complexity: O(n)
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mdict = Counter(arr)
        
        if len(set(mdict.values())) != len(mdict.values()):
            return False
        return True