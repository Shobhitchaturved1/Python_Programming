# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        maxval=root.val
        def dfs(root,maxval):
            nonlocal count
            if not root:
                return 0
            if root.val>=maxval:
                count+=1
                maxval=root.val
            if root.left:
                dfs(root.left,maxval)
            if root.right:
                dfs(root.right,maxval)
            return count
        return dfs(root,maxval)                    