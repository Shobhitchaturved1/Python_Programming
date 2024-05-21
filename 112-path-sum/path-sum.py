# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root,target):
            if root:
                target+=root.val
                if target==targetSum and (root.left==None and root.right==None):
                    return True    
                return helper(root.left,target) or helper(root.right,target)  
            else:
                return False
        return helper(root,0)    