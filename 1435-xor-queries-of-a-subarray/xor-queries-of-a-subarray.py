class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        prefix=[]
        a=0
        for i in arr:
            a^=i
            prefix.append(a)
        #print(prefix)    
        for x,y in queries:
            if x==0:
                ans.append(prefix[y])
            else:    
                ans.append(prefix[y]^prefix[x-1])
        return ans        