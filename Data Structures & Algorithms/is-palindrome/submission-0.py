class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = s.lower().replace(" " , "").replace("?" , "").replace("!" , "").replace("." , "").replace("," , "")
        newStr2 = ""
        for num in range(len(newStr) - 1, -1, -1):
            newStr2 = newStr2 + newStr[num]
        if (newStr == newStr2):
            return True
        return False
    