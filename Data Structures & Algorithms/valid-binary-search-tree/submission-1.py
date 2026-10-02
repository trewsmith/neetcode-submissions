# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid( node, left, right): # helper function to determine if a node follows bst rules

            if not node: 
                return True # null base case

            if not (node.val < right and node.val > left): # if the node does not satisfy boundary conditions immediately return false
                return False 
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        # ^ for left children, this sets the left boundary to whatever it was before and the right to the parent
        # for right children it keeps the right and uses the parent value for the left
        return valid(root, float("-inf") , float("inf")) #float("inf") is how you implement infinity in python 
    
    
    
        