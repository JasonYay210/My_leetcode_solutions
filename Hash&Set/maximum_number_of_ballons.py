from collections import defaultdict


class Solution:
    # Question: 1189

    # 0ms Beats 100%
    # Time Complexity: O(n + m) m being set_jewels
    # Space Complexity: O(m)
    def maxNumberOfBalloons(self, text: str) -> int:
        d_text = defaultdict(int)
        ballon = 'balon'

        for i in text:
            if i in "balloon":
                d_text[i] +=1

        count = float('inf')
        d_text['l'] = d_text['l'] // 2
        d_text['o'] = d_text['o'] // 2


        for i in ballon:
            if i not in d_text:
                return 0
    
        for i in d_text.keys():
            if d_text[i] < count:
                count = d_text[i]
        return count