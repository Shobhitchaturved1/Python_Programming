class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        if k==0 and tickets[0]==1:
            return 1
        for i in range(len(tickets)):
            if i==k:
                time+=tickets[k]
            else:
                if tickets[k]>tickets[i]:
                    time+=tickets[i]
                elif i>k:
                    time+=tickets[k]-1
                else:
                    time+=tickets[k]    
        return time                      