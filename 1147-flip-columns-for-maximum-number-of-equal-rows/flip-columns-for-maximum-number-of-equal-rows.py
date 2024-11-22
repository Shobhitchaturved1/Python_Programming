class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashmap=defaultdict(int)
        for r in matrix:
            if r[0]==1:
                r=[0 if i else 1 for i in r]
                 
            hashmap[tuple(r)]+=1
        return max(hashmap.values())          