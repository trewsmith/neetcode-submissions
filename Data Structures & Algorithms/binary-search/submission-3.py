class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0 
        max = len(nums) - 1 
        count = 0
        while(count < 15):
            i = int((max - min)/2)
            if (nums[i] == target):
                return i
            if (nums[i] < target):
                min = i
            if (nums[i] > target):
                max = i
            count = count + 1
        return -1


        