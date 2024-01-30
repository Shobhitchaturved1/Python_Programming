class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "*/+-":
                stack+=[int(i)]
            else:
                a=int(stack.pop())
                b=int(stack.pop())
                if i=="*":
                    stack+=[a*b]
                elif i=="+":
                    stack+=[a+b]
                elif i=="-":
                    stack+=[b-a]            
                else:   
                    stack+=[b/a]
        return int(stack[0])                