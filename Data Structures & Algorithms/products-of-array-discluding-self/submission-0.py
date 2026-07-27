class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for num in range(len(nums)):
            number = 1
            for i in range(len(nums)):
                if (i == num):
                    continue
                number = number * nums[i];
            output.append(number)
        return output
        