class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap=defaultdict(int)
        for i in arr:
            hashmap[i]+=1
        for c in arr:
            if hashmap[c]==1:
                k-=1
            if k==0:
                return c
        return ""                  