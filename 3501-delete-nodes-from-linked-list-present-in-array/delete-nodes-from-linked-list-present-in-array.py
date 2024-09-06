# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        nums=set(nums)
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        tmp=dummy
        while tmp.next is not None:
            if hashmap[tmp.next.val]:
                tmp.next=tmp.next.next
            else:
                tmp=tmp.next        
        return dummy.next    