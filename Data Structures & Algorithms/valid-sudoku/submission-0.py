class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        nums = []
        #row check
        for i in range(9):
            
            seen.clear()
            for j in range(9):
                if (board[i][j] != '.') and (board[i][j] in seen):
                    return False
                seen.add(board[i][j])
        #column check
        for i in range(9):
            
            seen.clear()
            for j in range(9):
                if (board[j][i] != '.') and (board[j][i] in seen):
                    return False
                seen.add(board[j][i])
        for i in range(1, 9, 3):
            
            for j in range(1,9,3):
                nums.clear()
                
                nums.append(board[i-1][j-1])
                nums.append(board[i-1][ j])
                nums.append(board[i-1][ j+1])
                nums.append(board[i][ j-1])
                nums.append(board[i][ j])
                nums.append(board[i][ j+1])
                nums.append(board[i+1][ j-1])
                nums.append(board[i+1][ j])
                nums.append(board[i+1][ j+1])
                seens = set();
                for num in nums: 
                    if (num != '.') and (num in seens):
                        return False
                    seens.add(num)
                    


        return True
                