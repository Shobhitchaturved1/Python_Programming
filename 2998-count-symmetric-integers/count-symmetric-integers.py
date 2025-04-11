class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        def check(s):
            total=0
            target=0
            for i in s:
                total+=int(i)
            for i in range(len(s)//2):
                target+=int(s[i])
            total-=target
            return 1 if (total)==target else 0        
        for i in range(low,high+1):
            if len(str(i))%2:
                continue
            count+=check(str(i))
        return  count        