class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:return True
        ans=[0,0,0]
        a,b,c=target[0],target[1],target[2]
        for x,y,z in triplets:
            if x<=a and y<=b and z<=c:
                ans[0],ans[1],ans[2]=max(ans[0],x),max(ans[1],y),max(ans[2],z)
                if ans==target:
                    return True
        return False            