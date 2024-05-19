# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        def merge(headA,headB):
            temp=ListNode()
            cur=temp
            while headA and headB:
                if headA.val<=headB.val:
                    cur.next=headA
                    headA=headA.next
                else:
                    cur.next=headB
                    headB=headB.next
                cur=cur.next
            if headA:
                cur.next=headA
            if headB:
                cur.next=headB        
            return temp.next
        for i in range(1,len(lists)):
            lists[0]=merge(lists[0],lists[i])
        return lists[0]                    