# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res=0
        def solve(root,steps,goleft):
            nonlocal res
            if not root:
                return
            res=max(res,steps)    
            if goleft==True:    
                solve(root.left,steps+1,False)
                solve(root.right,1,True)
            else:
                solve(root.right,steps+1,True)
                solve(root.left,1,False)
        solve(root,0,False)
        solve(root,0,True)            
        return res    