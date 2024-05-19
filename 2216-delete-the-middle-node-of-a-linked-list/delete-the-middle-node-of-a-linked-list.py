# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        length=0
        temp=head
        while temp:
            temp,length=temp.next,length+1
        length=length//2 -1
        #print(length)
        temp=head
        while length:
            temp=temp.next
            length-=1
        temp.next=temp.next.next
        return head    