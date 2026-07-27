class Solution:
    def isValid(self, s: str) -> bool:
        normArr = ['(' , '{' , '[']
        revArr = [')' , '}' , ']']

        secretStr = ""
        sstwo = ""
        if (len(s) % 2 != 0):
            return False
        else: 
            for num in range(0, len(s) // 2):
                if (s[num] not in normArr):
                    return false
                secretStr += str(normArr.index(s[num]))
            for num in range(len(s) // 2, len(s)):
                if (s[num] not in revArr):
                    return false
                sstwo += str(revArr.index(s[num]))
            return (secretStr == sstwo[::-1])

        