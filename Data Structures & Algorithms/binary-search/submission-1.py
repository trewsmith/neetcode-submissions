class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sol = -1
        trueInd = len(nums)
        count = 15
        while(count != 0):
            ind = int(trueInd / 2 )
            
            if(nums[ind] == target):
                return ind
            if(nums[ind] > target):
                trueInd = ind
            if(nums[ind] < target):
                trueInd = (ind * 2) - 1
            count = count - 1;
        return -1;



        