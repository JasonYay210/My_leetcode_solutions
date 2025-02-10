class Solution:
    # Question: 1657

    # 138ms Beats 48.16%
    # Time Complexity: O(n)  
    # Space Complexity: O(1)

    def closeStrings(self, word1: str, word2: str) -> bool:
        word1len = len(word1)
        word2len = len(word2)
        if word1len != word2len:
            return False
        testc = set(word1)
        testc2 = set(word2)
        if testc != testc2:
            return False

        mydict = {}
        mydict2 = {}
        for i in word1:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] += 1

        for i in word2:
            if i not in mydict2:
                mydict2[i] = 1
            else:
                mydict2[i] += 1
                
        arr = []
        for key, value in mydict.items():
            arr.append(value)
        arr2 = []
        for key, value in mydict2.items():
            arr2.append(value)

        arr.sort()
        arr2.sort()

        if arr == arr2:
            return True
        return False