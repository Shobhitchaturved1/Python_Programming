# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getlength(self,head):
            temp=head
            length=0
            while temp:
                temp=temp.next
                length+=1
            return length
    def reverseInK(self,head,k,length):
        if k>length:
            return head
        cur=head
        prev=None
        count=0
        while cur and count<k:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
            count+=1
        if tmp:
            head.next=self.reverseInK(tmp,k,length-k)
        return prev                     
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=self.getlength(head)
        return self.reverseInK(head,k,length)