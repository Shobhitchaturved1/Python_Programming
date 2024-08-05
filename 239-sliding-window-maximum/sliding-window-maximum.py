class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        ans=[]
        maxheap=[]
        for r in range(k):
            heapq.heappush(maxheap,(-nums[r],r))    
        for r in range(k,len(nums)):
            num,indx=heapq.heappop(maxheap)
            while indx<l:
                num,indx=heapq.heappop(maxheap)
            ans.append(-1*num)
            #print(ans)
            if l<indx:
                heapq.heappush(maxheap,(num,indx))
            heapq.heappush(maxheap,(-1*nums[r],r))    
            l+=1    
            #print(maxheap)
        num=max(nums[len(nums)-k:])    
        return ans+[num]
