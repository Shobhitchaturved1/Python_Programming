# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root):
            nonlocal ans
            if not root:
                return [0,0]
            lsum,lcnt=dfs(root.left)
            rsum,rcnt=dfs(root.right)
            nodesum=lsum+rsum+root.val
            nodecnt=lcnt+rcnt+1
            if nodesum//nodecnt==root.val:
                ans+=1
            return [nodesum,nodecnt]        
        dfs(root)
        return ans