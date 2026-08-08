class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1a = [0] * 26 
        l , r = 0, len(s1) - 1
        for num in range(len(s1)):
            s1a[ord(s1[num]) - 97] += 1
        for num in range(len(s2) - r ):
            s2a = [0] * 26
            for num2 in range(l , r + 1):
                s2a[ord(s2[num2]) - 97] += 1
            if (s1a == s2a):
                return True
            l+=1
            r+=1


        return False