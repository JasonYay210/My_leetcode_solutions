class Solution:
    # Question: 151

    # 0ms Beats 100%
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    def reverseWords(self, s: str) -> str:
        arr=s.split()
        arr.reverse()
        return " ".join(arr)
