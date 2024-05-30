class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count=0
        prefix=[0] +arr[:]
        size=len(prefix)
        for i in range(1,size):
            prefix[i]^=prefix[i-1]
        for i in range(size):
            for j in range(i+1,size):
                if prefix[i]==prefix[j]:
                    count+=j-i-1
        return count                
