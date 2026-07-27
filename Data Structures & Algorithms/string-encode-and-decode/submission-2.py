class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        
        for num in range(len(strs)):
            newStr = newStr + str(len(strs[num])) + "#" + strs[num] 
        return newStr


    def decode(self, s: str) -> List[str]:
        answer = []
        k = 0
        while (k < len(s)):
            if (ord('0') <= ord(s[k]) <= ord('9')):
                newStr = ""
                counter = ""
                while(s[k]!= "#"):
                    counter = counter + s[k]
                    k = k+1
                counterReal = int(counter)
                k = k + 1
                con = k + counterReal
                while(k < con):
                    newStr += s[k]
                    k+= 1
                answer.append(newStr)

        return answer

