class Solution:
    # Question: 345

    # 9ms Beats 71.87%
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) -1
        vowels = "AEIOUaeiou"
        temp = ""
        s_list = list(s)
        while left < right:
            if s[left] in vowels:
                if s[right] in vowels:
                    temp = s[left]
                    s_list[left] = s_list[right]
                    s_list[right] = temp
                    right-=1
                    left+=1
                else: 
                    right-=1
            else: 
                left+=1
        return ''.join(s_list) 