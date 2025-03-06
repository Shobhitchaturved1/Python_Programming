class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #a==repeating number and b==msiing number
        count=defaultdict(int)
        for i in grid:
            for j in i:
                count[j]+=1
        #print(count)        
        for i in range(1,len(grid)**2+1):
            if count[i]==0:
                b=i
            if count[i]==2:
                a=i
        return [a,b]            