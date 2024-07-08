class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        start=0
        while len(arr)!=1:
            removed=(start+k-1)%len(arr)
            arr.pop(removed)
            start=removed      
        return arr[0]