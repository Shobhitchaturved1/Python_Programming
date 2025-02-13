class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0
        arr=[]
        for i in nums:
            if i<k:
                arr.append(i)
        heapq.heapify(arr)        
        while len(arr)>1:        
            a=heapq.heappop(arr)
            b=heapq.heappop(arr)            
            new=min(a,b)*2+max(a,b)
            if new<k:
                heapq.heappush(arr,new)
            ans+=1
        return ans+1 if len(arr)==1 else ans        