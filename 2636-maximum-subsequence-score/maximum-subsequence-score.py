class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums=[]
        for num1,num2 in zip(nums1,nums2):
            nums.append([num2,num1])
        nums.sort(reverse=True)
        minHeap=[]
        num=0
        res=0
        ans=0
        for num2,num1 in nums:
            if len(minHeap)==k:
                res=max(res,ans)
                num-=heapq.heappop(minHeap)
            num+=num1
            heapq.heappush(minHeap,num1)
            ans=num*num2
        return max(ans,res)    