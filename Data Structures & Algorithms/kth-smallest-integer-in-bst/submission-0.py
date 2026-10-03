# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       n = 0 
       stack = []
       cur = root

       while cur or stack:
        while cur:
            stack.append(cur) 
            cur = cur.left 
        #once you've reached the furthest left node pop it from the stack as the nth value, n ranges from 1 to k 
        cur = stack.pop()
        n+= 1 
        if n == k: 
            return cur.val
        cur = cur.right

            