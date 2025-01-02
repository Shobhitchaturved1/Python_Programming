class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix=[]
        pre=0
        for i in words:
            if i[0] in "aeiou" and i[-1] in "aeiou":
                pre+=1
            prefix.append(pre)
        ans=[]
        for l,r in queries:
            if l==0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r]-prefix[l-1])
        return ans                    