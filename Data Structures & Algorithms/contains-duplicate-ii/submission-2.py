class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            c = 1 
            while c <= k and i - c >= 0: 
                if (nums[i - c] == nums[i]):
                    return True
                c+=1
        return False
