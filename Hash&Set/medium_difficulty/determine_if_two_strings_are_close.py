class Solution:
    # Question: 1657

    # 138ms Beats 48.16%
    # Time Complexity: O(n)  
    # Space Complexity: O(1)

    def closeStrings(self, word1: str, word2: str) -> bool:
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        if len_word1 != len_word2:
            return False
        
        unique_chars_word1 = set(word1)
        unique_chars_word2 = set(word2
        
        if unique_chars_word1 != unique_chars_word2:
            return False

        freq_word1 = {}
        freq_word2 = {}
        
        for char in word1:
            if char not in freq_word1:
                freq_word1[char] = 1
            else:
                freq_word1[char] += 1

        for char in word2:
            if char not in freq_word2:
                freq_word2[char] = 1
            else:
                freq_word2[char] += 1

        freq_list_word1 = list(freq_word1.values())
        freq_list_word2 = list(freq_word2.values())

        freq_list_word1.sort()
        freq_list_word2.sort()

        return freq_list_word1 == freq_list_word2
