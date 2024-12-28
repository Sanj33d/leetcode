# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # aprch1: calculation of num of nodes
        # if root is None:
        #     return 0 # bc
        # else:
        #     l_traversal = self.maxDepth(root.left) #lrc
        #     r_traversal = self.maxDepth(root.right) #rrc

        #     max_depth = 1 + max(l_traversal, r_traversal)
        #     return max_depth #op

        # aprch2: calculation: height + 1
        def helper(root): # calculates the height of the bt
            if root is None:
                return -1 # 
            else:
                l_traversal = helper(root.left) #lrc
                r_traversal = helper(root.right) #rrc

                max_depth = 1 + max(l_traversal, r_traversal)
                return max_depth
        
        ans = helper(root) + 1 # mmi: max_depth = num of longest_path_nodes = height + 1
        return ans
        