# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        q=deque()
        if not root:return []
        q.append(root)
        while q:
            maxi=float(-inf)
            for i in range(len(q)):
                node=q.popleft()
                if node.val>maxi:
                    maxi=node.val
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            ans.append(maxi)
        return ans    