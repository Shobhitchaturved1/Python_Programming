class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_map={}
        ans=[]
        for i in nums:
            if i not in hash_map:
                hash_map[i]=0
            idx=hash_map[i]
            if idx==len(ans):
                ans.append([])
            ans[idx].append(i)
            hash_map[i]+=1
        return ans            