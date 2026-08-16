class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for num in range(len(strs[0])):
            temp = pre
            pre = pre + strs[0][num] 
            for num in range(len(strs)):
                if pre not in strs[num]:
                    return temp
        return pre
        