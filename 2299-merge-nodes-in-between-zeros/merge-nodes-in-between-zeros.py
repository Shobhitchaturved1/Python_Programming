# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head=head.next
        if not head:
            return head
        tmp=head
        sum=0
        while tmp.val!=0:    
            sum+=tmp.val
            tmp=tmp.next
        head.val=sum
        head.next=self.mergeNodes(tmp)
        return head    