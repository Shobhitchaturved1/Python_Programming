class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx=0
        for i in s:
            if idx<len(g) and i>=g[idx]:
                idx+=1
        return idx        