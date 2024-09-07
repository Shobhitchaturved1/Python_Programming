# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def helper(root,cur):
            #if not root and cur:
                #return False
            if root.val!=cur.val:
                return False        
            cur=cur.next
            if not cur:
                return True
            return((helper(root.left,cur) if root.left else False)
            or (helper(root.right,cur) if root.right else False))

        def dfs(root):
            if root.val==head.val and helper(root,head):
                return True
            return ((dfs(root.left) if root.left else False)
            or (dfs(root.right) if root.right else False))
        return dfs(root)    