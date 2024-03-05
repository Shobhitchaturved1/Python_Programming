class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans=[1]*len(ratings)
        left=1
        while left<len(ratings):
            if ratings[left]>ratings[left-1]:
                ans[left]=ans[left-1]+1
            left+=1
        right=len(ratings)-2    
        while right>=0:
            if ratings[right]>ratings[right+1]:
                ans[right]=max(ans[right],ans[right+1]+1)   
            right-=1
        #print(ans)    
        return sum(ans)         


