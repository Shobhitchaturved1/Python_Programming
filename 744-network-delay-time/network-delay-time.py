class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans=[float("inf")]*n
        ans[k-1]=0
        adj=defaultdict(list)
        for src,dest,w in times:
            adj[src-1].append([dest-1,w])
        minheap=[[k-1,0]]
        print(adj)
        while minheap:
            src,w=heapq.heappop(minheap)
            for nei,wei in adj[src]:
                if ans[nei]>wei+w:
                    ans[nei]=wei+w
                    heapq.heappush(minheap,[nei,wei+w])
        for i in range(len(ans)):
            if ans[i]==float("inf"):
                return -1
        return max(ans)                    