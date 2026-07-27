class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0 
        max = len(nums) - 1 
       
        while(True):
            i = (min + ((max-min) //2))
            if (len(nums) == 1):
                if (target == nums[0]):
                    return 0;
                else:
                    return -1;
            
            if (nums[i] == target):
                return i
            elif (nums[i] < target):
                min = i + 1
                
            elif(nums[i] > target):
                max = i - 1
            if (max < min):
                return -1 
            
     


        