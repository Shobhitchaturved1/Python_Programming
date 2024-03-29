class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        for i in s:
            if i.lower() in "abcdefghijklmnopqrstuvwxyz0123456789":
                str+=i.lower()
        i=0
        j=len(str)-1 
        while i<j:
            if str[i]!=str[j]:
                return False
            i+=1
            j-=1
        return True               