class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1=0
        count_0=0
        for i in s:
            if i=="1":
                count_1+=1
            else:
                count_0+=1
        a=""
        while count_1>=2:
            a=a+"1"
            count_1-=1
        while count_0!=0:
            a+="0"
            count_0-=1
        return a+"1"                    