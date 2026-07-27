class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0 
        max = len(nums) - 1 
        count = 0
        while(count < 15):
            i = (max - (min//2) - 1)
            if (len(nums) == 1):
                return 0
            if (nums[i] == target):
                return i
            elif (nums[i] < target):
                min = i
            elif(nums[i] > target):
                max = i
            count = count + 1
        return -1


        