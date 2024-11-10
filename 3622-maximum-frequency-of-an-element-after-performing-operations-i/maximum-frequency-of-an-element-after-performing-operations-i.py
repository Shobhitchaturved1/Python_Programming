class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxnum=max(nums,default=0)
        size=maxnum+k+2
        freq=[0]*size
        for num in nums:
            freq[num]+=1
        pre=[0]*size
        pre[0]=freq[0]
        for i in range(1,size):
            pre[i]=pre[i-1]+freq[i]
        res=0
        for x in range(size):
            if freq[x]==0 and numOperations==0:
                continue
            left=max(0,x-k)
            right=min(size-1,x+k)
            totalInRange=pre[right]-(pre[left-1] if left>0 else 0)            
            canAdjust=totalInRange-freq[x]
            total=freq[x]+min(numOperations,canAdjust)
            res=max(res,total)
        return res       