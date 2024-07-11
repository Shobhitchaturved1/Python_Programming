class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=")":
                stack.append(i)
            else:
                newstack=[]
                while stack[-1]!="(":
                    a=stack.pop()
                    newstack.append(a)
                stack.pop()
                stack=stack+newstack
        return "".join(stack)            