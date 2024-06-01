class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        if self.small and self.large and (-1*self.small[0])>self.large[0]:
            val=heapq.heappop(self.small)
            heapq.heappush(self.large,-1*val)
        if abs(len(self.small)-len(self.large))>1:
                if len(self.small)>len(self.large):
                    val=heapq.heappop(self.small)
                    heapq.heappush(self.large,-1*val)
                else:
                    val=heapq.heappop(self.large)
                    heapq.heappush(self.small,-1*val)



    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        elif len(self.small)<len(self.large):
            return self.large[0]
        else:
            return (self.small[0]*-1 +self.large[0])/2        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()