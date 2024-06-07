class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1   
        q=deque()
        q.append([startGene,0])
        visit=set()
        visit.add(startGene)
        while q:
            gene,move=q.popleft()
            if gene==endGene:
                return move
            for i,ch in enumerate(gene):
                for j in "ACGT":
                    if ch!=j:
                        mut=gene[:i]+j+gene[i+1:]
                        if mut in bank and mut not in visit:
                            visit.add(mut)
                            q.append([mut,move+1])
        return -1                