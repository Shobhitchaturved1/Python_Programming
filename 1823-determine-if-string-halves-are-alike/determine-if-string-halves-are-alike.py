class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=s[0:len(s)//2]
        b=s[len(s)//2:]
        def vowel(x):
            count=0
            for i in x:
                if i.lower() in "aeiou":
                    count+=1
            return count
        return vowel(a)==vowel(b)            