class Solution:
    # Question: 392

    # 0ms Beats 100%
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        
        if s == '':
            return True
        
        for i in t:
            if s[count] == i:
                count +=1
            if count == len(s):
                return True
        return False