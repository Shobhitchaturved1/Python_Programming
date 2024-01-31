class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        stack=[]
        for i,t in enumerate(temp):
            while stack and t>stack[-1][0]:
                stackT,stackI=stack.pop()
                res[stackI]=(i-stackI)
            stack.append([t,i])
        return res    
                    
            