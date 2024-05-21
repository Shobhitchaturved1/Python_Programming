# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(nodeA,nodeB):
            if not nodeA and not nodeB:
                return None
            v1=nodeA.val if nodeA else 0
            v2=nodeB.val if nodeB else 0
            root=TreeNode(v1+v2)
            root.left=helper(nodeA.left if nodeA else None,nodeB.left if nodeB else None)
            root.right=helper(nodeA.right if nodeA else None,nodeB.right if nodeB else None)
            return root
        return helper(root1,root2)        