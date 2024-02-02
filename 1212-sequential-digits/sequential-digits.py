class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=12
        b=[12]
        a=[11]
        while b[-1]<=high:
            b.append(b[-1]*10+(b[-1]%10)+1)
            a.append(a[-1]*10+1)
        res=[]
        i=0
        while ans<=high:
            if ans>=low:
                res.append(ans)
            if ans%10!=9:
                ans+=a[i]    
            else:
                i+=1
                ans=b[i]
        return res            