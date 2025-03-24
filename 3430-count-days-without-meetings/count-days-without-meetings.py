class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans=0
        start,end=meetings[0][0],meetings[0][1]
        if start!=1:
            ans+=start-1
        for i in range(1,len(meetings)):
            x,y=meetings[i][0],meetings[i][1]
            if start<=x<=end or x<=start<=y:
                start=min(start,x)
                end=max(end,y)
            else:     
                ans+=x-end-1
                start,end=x,y
        return ans if end==days else ans+days-end

