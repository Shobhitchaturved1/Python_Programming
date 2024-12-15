class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain_ratio(passi,totali):
            return ((passi+1)/(totali+1))-(passi/totali)
        heap=[]
        for passi,totali in classes:
            gain=gain_ratio(passi,totali)
            heappush(heap,(-gain,passi,totali))

        for i in range(extraStudents):        
            gain,passi,totali=heappop(heap)
            passi+=1
            totali+=1
            new_gain=gain_ratio(passi,totali)
            heappush(heap,(-new_gain,passi,totali))

        total_ratio=0
        for gain,passi,totali in heap:
            total_ratio+=passi/totali
        return total_ratio/len(classes)        