# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Brute force method
        temp=head
        arr=set()
        while temp:
            if temp not in arr:
                arr.add(temp)
                temp=temp.next
            else:
                return temp
        return None                