class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[1]*n
    def find(self,x):
        if self.par[x]!=x:
            self.par[x]=self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        p1,p2=self.find(x),self.find(y)
        if p1==p2:
            return 0
        if self.rank[p1]<self.rank[p2]:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        else:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p1] 
        return 1                       
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf=UnionFind(len(stones))
        samerow={}
        samecol={}
        for i,(r,c) in enumerate(stones):
            if r in samerow:
                uf.union(i,samerow[r])
            else:
                samerow[r]=i
        for i,(r,c) in enumerate(stones):
            if c in samecol:
                uf.union(i,samecol[c])
            else:
                samecol[c]=i
        ans=0
        for i,(r,c) in enumerate(stones):
            if uf.find(i)==i:
                ans+=1
        return len(stones)-ans                            