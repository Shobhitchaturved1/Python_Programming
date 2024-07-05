# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical=[]
        prev=head
        if head.next:
            cur=head.next
        else:
            return [-1,-1]    
        if head.next.next:    
            forward=head.next.next
        else:
            return [-1,-1]
        i=2    
        while forward:
            if prev.val>cur.val and cur.val<forward.val:
                critical.append(i)
            elif prev.val<cur.val and cur.val>forward.val:
                critical.append(i)
            prev=prev.next
            cur=cur.next
            forward=forward.next
            i+=1
        if len(critical)<=1:
            return [-1,-1]
        maxima=critical[-1]-critical[0]
        minima=float("inf")
        for i in range(len(critical)-1):
            minima=min(minima,critical[i+1]-critical[i])
        return [minima,maxima]    

