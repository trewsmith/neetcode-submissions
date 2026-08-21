class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for num in range(len(nums)):
            if nums[num] == 0:
                red +=1
            if nums[num] == 1:
                white +=1
            if nums[num] == 2:
                blue +=1
        for i in range(red):
            nums[i] = 0 
        for j in range(white):
            nums[red + j] = 1
        for k in range(blue):
            nums[red + white + k] = 2