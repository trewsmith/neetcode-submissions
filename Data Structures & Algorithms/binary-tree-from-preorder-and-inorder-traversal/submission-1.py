# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
'''
#proper solution with hash map
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val: i for i, val in enumerate(inorder)}

        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r or in_l > in_r:
                return None

            root_val = preorder[pre_l]
            root = TreeNode(root_val)

            mid = pos[root_val]
            left_size = mid - in_l

            root.left = build(
                pre_l + 1,
                pre_l + left_size,
                in_l,
                mid - 1
            )

            root.right = build(
                pre_l + left_size + 1,
                pre_r,
                mid + 1,
                in_r
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)