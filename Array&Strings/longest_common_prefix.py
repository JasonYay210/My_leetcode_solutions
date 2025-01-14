from typing import List


class Solution:
    # Question: 14

    # 0ms Beats 100%
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        for s in strs:
            if min_length > len(s):
                min_length = len(s)
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1
        return s[:i]
            
            
