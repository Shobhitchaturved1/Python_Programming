class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans=[]
        freq=defaultdict(int)
        count=0
        for i in range(len(A)):
            freq[A[i]]+=1
            freq[B[i]]+=1
            if A[i]==B[i]:
                count+=1
            else:
                if freq[A[i]]==2:
                    count+=1
                if freq[B[i]]==2:
                    count+=1
            ans.append(count)
        return ans            
