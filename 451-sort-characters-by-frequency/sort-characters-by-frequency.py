class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        buckets=defaultdict(list)
        for char,cnt in count.items():
            buckets[cnt]+=char
        res=""    
        for i in range(len(s),0,-1):
            for c in buckets[i]:    
                res+=c*i
        return res        