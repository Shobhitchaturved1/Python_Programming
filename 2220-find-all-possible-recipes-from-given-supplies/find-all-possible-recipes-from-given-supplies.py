class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree={r:0 for r in recipes}
        hashmap=defaultdict(list)
        for x,y in zip(recipes,ingredients):
            for j in y:
                hashmap[j].append(x)
            indegree[x]=len(y)    
        q=deque(supplies)
        res=set(supplies)
        while q:
            item=q.popleft()
            for r in hashmap[item]:
                indegree[r]-=1
                if indegree[r]==0:
                    q.append(r)
                    res.add(r)
        
        return [r for r in recipes if r in res]                              