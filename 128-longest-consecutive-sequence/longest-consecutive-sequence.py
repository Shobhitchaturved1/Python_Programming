class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(i):
            if i!=parent[i]:
                parent[i]=find(parent[i])
            return parent[i]
        def union(i,j):
            pi,pj=find(i),find(j)
            if pi!=pj:
                if rank[pi]>=pj:
                    parent[pj]=pi
                    rank[pi]+=1
                else:
                    parent[pi]=pj
                    rank[pj]+=1
        if not nums:
            return 0
        parent,rank,nums={},{},set(nums)                       
        for num in nums:
            parent[num]=num
            rank[num]=0
        for num in nums:
            if num-1 in nums:
                union(num-1,num)
            if num+1 in nums:
                union(num+1,num)
        d=collections.defaultdict(list)
        for num in nums:
            d[find(num)].append(num)
        return max([len(l) for l in d.values()])                         