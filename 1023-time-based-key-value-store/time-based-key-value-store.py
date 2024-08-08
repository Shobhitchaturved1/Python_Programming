class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value,timestamp])        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr=self.hashmap[key]
        res=""
        l,r=0,len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m][1]<=timestamp:
                res=arr[m][0]
                l=m+1
            else:
                r=m-1
        return res            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)