class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for num in range(len(strs)):
            newStr = newStr + strs[num] + "enc"
        return newStr


    def decode(self, s: str) -> List[str]:
        newS = s.replace("enc" , " ")
        newSS = newS.split()
        return newSS

