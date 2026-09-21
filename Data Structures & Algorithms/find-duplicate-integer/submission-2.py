class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 2: 
            return nums[0]
        for i in range( 1, len(nums) - 1):
            if (nums[i - 1 ] == nums[i]) or (nums[i + 1 ] == nums[i]):
                return nums[i]
        