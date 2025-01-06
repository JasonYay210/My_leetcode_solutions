class Solution:
    # Question: 151

    # 0ms Beats 100%

    def reverseWords(self, s: str) -> str:
        arr=s.split()
        arr.reverse()
        return " ".join(arr)
