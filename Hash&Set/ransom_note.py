from collections import defaultdict


class Solution:
    # Question: 383

    # 23ms Beats 50%
    # Time Complexity: O(n + m) m being the defaultdicts
    # Space Complexity: O(n + m) m being the defaultdicts

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        C_ranson = defaultdict(int)

        for item in ransomNote:
            C_ranson[item] += 1

        c_magazine = defaultdict(int)

        for item in magazine:
            c_magazine[item] +=1

        for i in C_ranson.keys():
            if C_ranson[i] > c_magazine[i]:
                return False
        return True
            