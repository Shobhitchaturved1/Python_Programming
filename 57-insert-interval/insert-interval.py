class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        flag=True
        if len(intervals)==0:
            return [newInterval]
        for x,y in intervals:
            if newInterval[0]<=x and flag:
                ans.append(newInterval)
                flag=False
            ans.append([x,y])
            
        if len(ans)==len(intervals):
            if newInterval[0]<intervals[0][0]:
                ans=[newInterval]+ans
            else:
                ans+=[newInterval]
        print(ans)        
        start,end=ans[0][0],ans[0][1]
        res=[]
        for x,y in ans:
            if x<=start<=y or start<=x<=end:
                start=min(start,x)
                end=max(y,end)
            else:
                res.append([start,end])
                start=x
                end=y    
        #print(ans)
        return res+[[min(start,x),max(y,end)]]    