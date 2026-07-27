class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = [0] * 26;
        tArr = [0] * 26;
        if (len(s) != len(t)):
            return False
        for num in range(len(s)):
            sArr[ord(s[num]) - 97] += 1
            tArr[ord(t[num]) - 97] += 1
        if (sArr != tArr):
                return False
        return True



        
