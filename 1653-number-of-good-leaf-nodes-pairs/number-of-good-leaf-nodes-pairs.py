# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs=0
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left_side=dfs(node.left)
            right_side=dfs(node.right)
            for i in left_side:
                for j in right_side:
                    if i+j<=distance:
                        self.pairs+=1
            all_pair=left_side+right_side            
            return [d+1 for d in all_pair]                   
        dfs(root)
        return self.pairs       