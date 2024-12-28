# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root # bc
        else:
            l_traversal = self.invertTree(root.left) #l_rc
            r_traversal = self.invertTree(root.right)#r_rc

            root.left, root.right = root.right, root.left ##op
            return root
        