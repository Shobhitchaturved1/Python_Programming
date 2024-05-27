class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtrack(start,cur_list):
            if len(cur_list)==k:
                ans.append(cur_list.copy())
                return 
            for i in range(start,n+1):
                cur_list.append(i)
                backtrack(i+1,cur_list)
                cur_list.pop()
        backtrack(1,[])
        return ans        