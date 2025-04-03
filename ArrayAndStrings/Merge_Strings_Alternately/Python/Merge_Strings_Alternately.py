class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        array = []
        i=0
        string =""
        while len(word1) > i or len(word2) > i:
            if len(word1) > i:
                array.append(word1[i])
            if len(word2) > i:
                array.append(word2[i])
            i += 1
            string = ''.join(array)
        return string
