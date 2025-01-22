from collections import defaultdict


class Solution:
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
