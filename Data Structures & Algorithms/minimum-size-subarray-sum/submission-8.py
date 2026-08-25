class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minNum = 99999999
        curSum = 0 
        l , r = 0 , 0
        k = 0

        sSum = 0
        for i in range(len(nums)):
            sSum+= nums[i]
        if sSum < target:
            return 0

        while r < len(nums) or curSum >= target: 
            if curSum < target: 
                 
                
                curSum += nums[r]
                k+=1
                r+=1
            if curSum >= target: 
                minNum = min(minNum, k)
                l+=1
                curSum -= nums[l - 1]
                k-=1
        return minNum
        
                
