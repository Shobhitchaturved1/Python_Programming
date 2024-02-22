class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        beingTrustedBy=defaultdict(int)
        isTrusting=defaultdict(int)
        for x,y in trust:
            isTrusting[x]+=1
            beingTrustedBy[y]+=1
        for i in range(1,n+1):
            if beingTrustedBy[i]==n-1 and isTrusting[i]==0:
                return i
        return -1            

          