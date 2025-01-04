class Solution:
    # Question: 1071

    # 5ms Beats 13.26%
    # Time Complexity: O(L * (n + m)), where L = min(len(str1), len(str2)), n = len(str1), and m = len(str2)
    # Space Complexity: O(L), where L = min(len(str1), len(str2)) 
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Check if concatenated strings are equal or not; if not, return ""
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the minimum length of the two strings
        min_length = min(len(str1), len(str2))
        
        # Check each possible prefix
        for i in range(min_length, 0, -1):
            # Take the substring of str1 up to the current length
            candidate = str1[:i]
            # Check if it divides both strings
            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:
                if candidate * (len(str1) // len(candidate)) == str1 and candidate * (len(str2) // len(candidate)) == str2:
                    return candidate
        
        return ""