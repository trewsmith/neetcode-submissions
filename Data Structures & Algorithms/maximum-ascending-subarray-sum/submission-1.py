class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l = 0
        maxSum = 0
        nums.append(0)
        for r in range(1, len(nums)):
            
            if nums[r] <= nums[r - 1]:
                posSum = 0
                for num in range(l, r):
                    posSum += nums[num]
                maxSum = max(maxSum, posSum)
                l = r
            

        return maxSum