class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[1]*n
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x,y):
        p1,p2=self.find(x),self.find(y)
        if p1==p2:
            return False
        if self.rank[p1]<self.rank[p2]:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        else:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        return True                        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf=UnionFind(len(accounts))
        emailacc={}
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in emailacc:
                    uf.union(i,emailacc[e])
                else:
                    emailacc[e]=i
        emailgroup=defaultdict(list)
        for e,i in emailacc.items():
            leader=uf.find(i)
            emailgroup[leader].append(e)
        res=[]
        for i,emails in emailgroup.items():
            name=accounts[i][0]
            res.append([name]+ sorted(emailgroup[i]))
        return res                        