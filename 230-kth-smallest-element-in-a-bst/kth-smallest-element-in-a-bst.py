# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        def inorder(root):
            if root:
                inorder(root.left)
                stack.append(root.val)
                inorder(root.right)
        inorder(root)
        while k:
            a=stack.pop(0)
            k-=1
        return a            