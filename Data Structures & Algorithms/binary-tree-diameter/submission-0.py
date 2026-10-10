# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0

        def depth(node):
            nonlocal diameter

            if node is None:
                return 0
            left_d=depth(node.left)
            right_d=depth(node.right)

            diameter=max(diameter,left_d+right_d)
            return 1+max(left_d,right_d)
        depth(root)
        return diameter
        