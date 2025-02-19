class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=="]":
                a=""
                while stack[-1]!="[":
                    a=stack.pop()+a
                stack.pop()    
                num=""   
                while stack and stack[-1] in "0123456789":
                    num=stack.pop()+num
                stack.append(int(num)*a)
            else:    
                stack.append(i)    
        return "".join(stack)        