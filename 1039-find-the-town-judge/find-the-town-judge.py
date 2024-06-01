class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        beingtrustedby=defaultdict(int)
        istrusting=defaultdict(int)
        for x,y in trust:
            istrusting[x]+=1
            beingtrustedby[y]+=1
        for i in range(1,n+1):
            if beingtrustedby[i]==n-1 and istrusting[i]==0:
                return i
        return -1            