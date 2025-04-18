class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(x):
            newx=""
            i=0
            while i<len(x):
                count=1
                while i+1<len(x) and x[i]==x[i+1]:
                    count+=1
                    i+=1
                newx+=str(count)+x[i]
                i+=1
            #print(newx)   
            return newx   
        if n==0:return ""         
        s="1"
        for i in range(n-1):
            s=rle(s)
        return s    