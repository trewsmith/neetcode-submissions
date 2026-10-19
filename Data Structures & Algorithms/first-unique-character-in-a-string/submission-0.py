class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [0] * 26
        
        for i in range(len(s)): 
            chars[ord(s[i]) - ord('a')] += 1
        for i in range(len(s)):
            if chars[ord(s[i]) - ord('a')] == 1: 
                return i

        return -1