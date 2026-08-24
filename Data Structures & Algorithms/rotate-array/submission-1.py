class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * len(nums)
        for i in range(len(nums)):
            tempI = i + k
            if tempI > len(nums) - 1:
                tempI = tempI % len(nums)
            temp[tempI] = nums[i]

        for i in range(len(temp)):
            nums[i] = temp[i]
        