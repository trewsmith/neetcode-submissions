class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        numSet = {}
        for i in range(len(nums)):
            if nums[i] not in numSet: 
                numSet[nums[i]] = 0
            numSet[nums[i]] += 1
            if numSet.get(nums[i]) > (len(nums) / 3): 
                if nums[i] not in res:
                    res.append(nums[i])
        return res