class Solution:
    def parseBoolExpr(self, e: str) -> bool:
        stack=[]
        if len(e)==1:
            return True if e[0]=="t" else False
        def solve_and(arr):
            for i in arr:
                if i=="f":
                    return "f"
            return "t"
        def solve_or(arr):
            for i in arr:
                if i=="t":
                    return "t"
            return "f"
        def solve_not(arr):
            return "t" if arr[0]=="f" else "f"                          
        for i in range(len(e)-1,-1,-1):
            if e[i]=="(":
                opp=e[i-1]
                newstack=[]
                while stack and stack[-1]!=")":
                    newstack.append(stack.pop())  
                stack.pop()      
                if opp=="&":
                    stack+=[solve_and(newstack)]
                elif opp=="|":
                    stack+=[solve_or(newstack)]
                else:
                    stack+=[solve_not(newstack)]
            if e[i]=="f" or e[i]=="t" or e[i]==")":        
                stack.append(e[i])    
            #print(stack)        
        return True if stack[0]=="t" else False

