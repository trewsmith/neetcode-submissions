class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l2= []
        for num in range(len(nums)):

            if nums[num] != val:
                l2.append(nums[num])

        for i in range(len(l2)):
            nums[i] = l2[i]
        return len(l2)