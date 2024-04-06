class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        open_para=0
        ans=""
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
                open_para+=1
            elif s[i]==")":
                if open_para>=1:
                    stack.pop()
                    open_para-=1
                else:
                    stack.append(i)        
        for i in range(len(s)):
            if i not in stack:
                ans+=s[i]
        return ans        
