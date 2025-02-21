# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.ans=[0]
        if root:
            root.val=0
        def dfs(root):
            if not root:
                return
            if root.left:
                root.left.val=root.val*2+1
                self.ans.append(root.left.val)
                dfs(root.left)
            if root.right:
                root.right.val=root.val*2+2  
                self.ans.append(root.right.val)
                dfs(root.right)       
        dfs(root)           


    def find(self, target: int) -> bool:
        return target in self.ans


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)