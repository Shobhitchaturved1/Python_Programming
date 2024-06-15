class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        number,result,sign=0,0,1
        for i in s:
            if i=="(":
                stack.append(result)
                stack.append(sign)
                result,number,sign=0,0,1
                #print(stack)
            elif i==")":
                #print(result)
                result+=(number*sign)
                number=0
                result=result*stack.pop()
                result+=stack.pop()
                #print(result)
            elif i=="+":
                result+=(number*sign)
                sign=1
                number=0
            elif i=="-":
                result+=(number*sign)
                sign=-1
                number=0
            elif i in "0123456789":        
                number=number*10+int(i) 
        return result+number*sign         