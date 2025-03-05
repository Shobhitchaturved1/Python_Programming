class Solution:
    def coloredCells(self, n: int) -> int:
        #at minite 1 -> 1 cell is color
        #at minute 2-> 5 cell is color
        #at minute 3->13 cell is color  
        #1,3,5
        if n==1:return 1
        ans=1
        num=1
        while n-1:
            ans+=num+2
            num+=2
            n-=1
        return ans*2-num  