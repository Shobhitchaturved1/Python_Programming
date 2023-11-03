class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out=[]
        s=[]
        j=0
        for i in range(1,n+1):
            if j<len(target):
                s+=[i]
                print(s)
                out+=["Push"]
                if s[-1]==target[j]:
                    j+=1   
                else:
                    s.remove(i)
                    out+=["Pop"]
            #if(j==len(target)):
        return out   
        