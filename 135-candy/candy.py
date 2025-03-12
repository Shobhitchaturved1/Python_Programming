class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans=1
        i=1
        while i<len(ratings):
            if (ratings[i]==ratings[i-1]):
                ans+=1
                i+=1
                continue
            peak=1
            while(i<len(ratings) and ratings[i]>ratings[i-1]):
                peak+=1
                i+=1
                ans+=peak
            down=1  
            while(i<len(ratings) and ratings[i]<ratings[i-1]):
                ans+=down
                down+=1
                i+=1                        
            if down>peak:
                ans+=down-peak
        return ans            