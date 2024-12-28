# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def helper(root): # compares the height of two subtrees of every nodes
            nonlocal flag
            if root == None: # bc
                return 0
            else:
                l_traversal = helper(root.left) #lrc
                r_traversal = helper(root.right) #rrc

                if abs(l_traversal - r_traversal) > 1: #op stat
                    flag = False
                
                height = 1 + max(l_traversal, r_traversal)
                return height #op end
                    
        ans = helper(root)
        return flag
        