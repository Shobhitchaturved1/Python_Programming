class Solution:
    def makeFancyString(self, s: str) -> str:
        count=0
        new=""
        for i in s:
            if len(new)==0:
                count+=1
                prev=i
                new+=i
            elif prev==i:
                count+=1
                if count<3:
                    new+=i
            else:
                count=1
                prev=i
                new+=i
        return new                
