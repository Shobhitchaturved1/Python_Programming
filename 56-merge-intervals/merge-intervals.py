class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]  
        for i in range(1,len(intervals)):
            start,end=ans[-1][0],ans[-1][1]
            first,second=intervals[i][0],intervals[i][1]
            if first<=end:
                ans.pop()
                ans.append([start,max(end,second)])
            else:
                ans.append([first,second])    
        return ans        
