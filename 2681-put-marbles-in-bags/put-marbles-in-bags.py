class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1:
            return 0
        poss=[]
        for i in range(len(weights)-1):
            poss.append(weights[i]+weights[i+1])
        poss.sort()   
        i=k-1
        mini=sum(poss[:i])
        maxi=sum(poss[-i:])
        return maxi-mini    