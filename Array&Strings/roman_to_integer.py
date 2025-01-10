class Solution:
    # Question: 13

    # 7ms Beats 43.30%
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def romanToInt(self, s: str) -> int:
        my_dict = {
            'I':1,
            'V':5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        result = 0
        i = 0
        while i < len(s):
            if i != len(s)-1 and my_dict[s[i+1]] > my_dict[s[i]]:
                result += (my_dict[s[i+1]] - my_dict[s[i]])
                i += 2
            else:
                result += my_dict[s[i]]
                i +=1
        return result 