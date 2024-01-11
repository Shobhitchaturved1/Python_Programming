# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def max_diff(root,diff,max_a,min_b):
            if root:
                if max_a<root.val:
                    max_a=root.val
                if root.val<min_b:
                    min_b=root.val
                diff=max(diff,abs(max_a-min_b))  
            else:
                return  diff
            return max(max_diff(root.left,diff,max_a,min_b),max_diff(root.right,diff,max_a,min_b))
        return max_diff(root,0,root.val,root.val)            