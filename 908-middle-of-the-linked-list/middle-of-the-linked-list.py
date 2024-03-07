# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        leng=0
        while(temp):
            leng+=1
            temp=temp.next
        temp=head
        n=leng//2
        while(n):
            temp=temp.next
            n-=1
        return temp        