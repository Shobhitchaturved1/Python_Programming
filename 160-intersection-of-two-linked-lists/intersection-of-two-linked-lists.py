# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length1=0
        length2=0
        temp1=headA
        while temp1:
            temp1=temp1.next
            length1+=1
        temp2=headB
        while temp2:
            temp2=temp2.next
            length2+=1        
        length = length1 -length2
        if length<0:
            #headB is more
            while length!=0:
                headB=headB.next
                length+=1
        else:
            while length!=0:
                headA=headA.next
                length-=1          
        while headA:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return headA                