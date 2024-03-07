class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        left=0
        right=len(height)-1
        maxleft=height[left]
        maxright=height[right]
        ans=0
        while left<right:
            if maxleft<=maxright:
                left+=1
                maxleft=max(maxleft,height[left])
                ans+=maxleft-height[left]
            else:
                right-=1
                maxright=max(maxright,height[right])
                ans+=maxright-height[right]
        return ans                