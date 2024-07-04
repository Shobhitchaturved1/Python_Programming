# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        ans=res
        tmp=head.next
        s=0
        while tmp:
            s+=tmp.val
            if tmp.val==0:
                ans.next=ListNode(s)
                ans=ans.next
                s=0
            tmp=tmp.next
        return res.next 