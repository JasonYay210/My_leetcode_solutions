from collections import defaultdict


class Solution:
    # Question: 242

    # 9ms Beats 78.54%
    # Time Complexity: O(n + m) m being the defaultdicts
    # Space Complexity: O(1) limited to alphabet

    def isAnagram(self, s: str, t: str) -> bool:
        c_s = defaultdict(int)
        
        for i in s:
            c_s[i] +=1

        t_s = defaultdict(int)

        for i in t:
            t_s[i] +=1
            
        if len(s) != len(t):
            return False
        
        for i in c_s.keys():
            if t_s.get(i,0) == 0:
                return False
            if c_s[i] != t_s[i]:
                return False
        return True
