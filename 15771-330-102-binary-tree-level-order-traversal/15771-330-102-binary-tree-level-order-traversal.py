# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # approach: top-down aproach (op then recursive call)
        # bc: None: return root
        # lrc, rrc
        # op: res = l; counter for level
        l = []
        def helper(root, level):
            if root == None: #bc
                return root
            else:  # op starts
                if level == len(l): 
                    l.append([])
                l[level].append(root.val) # op ends

                left = helper(root.left, level + 1) # lrc
                right = helper(root.right, level + 1) #rrc
                # return root; not mandatory as l is the required res
        ans = helper(root, 0)
        return l
        