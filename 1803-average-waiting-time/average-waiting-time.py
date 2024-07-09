class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start=customers[0][0]
        #end=customers[0][0]
        res=[]
        for x,y in customers:
            if x<=start:
                res.append(start+y-x)
                start+=y
            else:
                start=x
                res.append(start+y-x)
                start+=y
                
        #print(res)        
        return sum(res)/len(res)            
