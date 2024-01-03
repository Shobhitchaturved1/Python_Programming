class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        i,j=0,1
        def count1(x):
            count=0
            for a in x:
                if a=="1":
                    count+=1
            return count        
        while i<len(bank) and j<len(bank):
            fir=count1(bank[i])
            sec=count1(bank[j])
            if fir==0:
                i+=1
                if i==j:
                    j+=1
            elif sec==0:
                j+=1
            else:
                i+=1
                ans+=fir*sec
                j+=1
        return ans            