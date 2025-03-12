class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for i,x in enumerate(s):
            if x=="(":
                stack.append(i)
            elif x=="*":
                star.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stack and star:
            if stack.pop()>star.pop():
                return False
        return not stack        