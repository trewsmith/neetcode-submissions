class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fins = ""
        for i in range(len(word1)):
            j = i
            fins += word1[i]
            if j < len(word2):
                fins +=word2[j]
        if len(word2) > len(word1):

            for k in range(j + 1, len(word2)):
                fins += word2[k]
        return fins