# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left=ListNode()
        right=ListNode()
        ltail,rtail=left,right
        temp=head
        while temp:
            if temp.val<x:
                ltail.next=temp
                ltail=ltail.next
            else:
                rtail.next=temp
                rtail=rtail.next
            temp=temp.next
        ltail.next=right.next
        rtail.next=None
        return left.next    