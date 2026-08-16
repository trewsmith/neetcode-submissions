class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapp = {} 
        maximum = 0
        maximumC = 0
        for i in range(len(nums)):
            if nums[i] not in mapp:
                mapp[nums[i]] = 0
            mapp[nums[i]] +=1
            if mapp.get(nums[i]) > maximumC:
                maximum = nums[i]
                maximumC = mapp.get(nums[i])
        return maximum