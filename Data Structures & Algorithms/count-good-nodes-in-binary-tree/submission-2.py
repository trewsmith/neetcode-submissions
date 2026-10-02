# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    
    def goodNodes(self, root: TreeNode) -> int:
        def check(root: TreeNode, tempMax):
            if not root: 
                return 0
            if root.val >= tempMax:
                tempMax = root.val 
                res = 1
            else:
                res = 0
            
            
            return res + check(root.left, tempMax) + check(root.right, tempMax)
        
        return check(root, -101)
        