class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        maps=defaultdict(int)
        for i in arr:
            maps[i]+=1
        arr=[]
        for i in maps.values():
            if i in arr:
                return False
            arr+=[i]
        return True           