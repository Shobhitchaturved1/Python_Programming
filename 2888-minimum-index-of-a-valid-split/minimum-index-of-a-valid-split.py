class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        pre=[[False,-1]]*len(nums)
        suf=[[False,-1]]*len(nums)
        map1=defaultdict(int)
        map2=defaultdict(int)
        maxi=float("-inf")
        maxi2=float("-inf")
        val,val2=-1,-1
        for i in range(len(nums)):
            map1[nums[i]]+=1
            if map1[nums[i]]>maxi:
                maxi=map1[nums[i]]
                val=nums[i]
            pre[i]=[True,val] if maxi*2>i+1 else [False,-1]
            idx=len(nums)-i-1   
            #print(idx) 
            map2[nums[idx]]+=1
            if map2[nums[idx]]>maxi2:
                maxi2=map2[nums[idx]]
                val2=nums[idx]
            suf[idx]=[True,val2] if maxi2*2>len(nums)-idx else [False,-1]    
        ans=-1
        
        #print(pre)
        #print(suf)

        for i in range(len(pre)-1):
            if pre[i]==suf[i+1] and pre[i][0]:
                ans=i
                break
        return ans                