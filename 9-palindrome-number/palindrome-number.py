class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        i=0
        j=len(num)-1
        while i<j:
            if num[i]!=num[j]:
                return False
            i+=1
            j-=1
        return True