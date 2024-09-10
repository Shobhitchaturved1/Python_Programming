# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b<a:
                a,b=b,a
            ans=1    
            for i in range(1,a+1):
                if a%i==0 and b%i==0:
                    ans=i    
            return ans
        first=head
        if head.next:
            second=head.next
        else:
            return head    
        cur=head
        temp=cur
        while second:
            new=gcd(first.val,second.val)
            temp.next=ListNode(new)
            temp=temp.next
            temp.next=second
            temp=temp.next
            first=second
            second=second.next
        return cur               