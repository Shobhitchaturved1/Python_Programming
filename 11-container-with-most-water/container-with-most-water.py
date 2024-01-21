class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        j=len(height)-1
        i=0
        a=len(height)-1
        while i<=j and a!=0:
            if height[i]<height[j]:
                area=max(area,a*height[i])
                i+=1
            else:
                area=max(area,a*height[j])
                print(area)
                j-=1
            a-=1
        return area            