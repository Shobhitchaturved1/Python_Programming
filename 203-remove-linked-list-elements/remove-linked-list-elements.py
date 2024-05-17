# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=head
        while temp and temp.val==val:
            temp=temp.next
        head=temp    
        while temp:
            if temp.next and temp.next.val==val:
                temp.next=temp.next.next
            else:    
                temp=temp.next    
        return head        