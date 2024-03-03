# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng=0
        temp=head
        while temp:
            temp=temp.next
            leng+=1
        a=leng-n-1
        if leng==n:
            if head.next:
                return head.next
            return None
        temp=head
        while a:
            temp=temp.next
            a-=1
        temp.next=temp.next.next
        return head