class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxLen = 0
        if (len(nums) == 0 ):
            return 0
        for i in range (len(nums)):
            seq = [nums[i]]
            for num in range(i, len(nums)):
                if((nums[num]) == (seq[len(seq) - 1] + 1)):
                    seq.append(nums[num])
                if (len(seq) > maxLen):
                    maxLen = len(seq)
        return maxLen


        