class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
  
        l, r = 0, len(matrix ) - 1 
        while l <= r: 
            if matrix[l + (r - l) // 2][0] == target: 
                return True
            elif matrix[l + (r - l) // 2][0] > target: 
                r =  (l + (r - l) // 2) - 1
                
            else: 
                for i in range(len(matrix[l + (r - l) // 2])):
                    if matrix[l + (r - l) // 2][i] == target:
                        return True

                l =  (l + (r - l) // 2) + 1
                
        return False