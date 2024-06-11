class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=defaultdict(int)
        arr1.sort()
        ans=[]
        for i in arr1:
            count[i]+=1
        for i in arr2:
            ans+=[i]*count[i]
        for i in arr1:
            if i not in arr2:
                ans+=[i]
        return ans                