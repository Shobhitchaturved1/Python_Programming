class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        l=float("-inf")
        r=float("inf")
        for i in  range(len(original)):
            a=original[i]
            u=bounds[i][0]
            v=bounds[i][1]
            l=max(l,u-a)
            r=min(r,v-a)
        if l>r:
            return 0
        return r-l+1        