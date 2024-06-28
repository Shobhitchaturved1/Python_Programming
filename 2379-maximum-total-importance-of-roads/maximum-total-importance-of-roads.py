class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr=[0]*(n)
        for x,y in roads:
            arr[x]+=1
            arr[y]+=1
        ans=0   
        count=1    
        for i in sorted(arr):
            ans+=i*count
            count+=1
        return ans    
