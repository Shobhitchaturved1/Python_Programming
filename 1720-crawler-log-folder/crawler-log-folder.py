class Solution:
    def minOperations(self, logs: List[str]) -> int:
        arr=[]
        for i in logs:
            if i=="../":
                if arr:
                    arr.pop()
            elif i=="./":
                continue
            else:
                arr.append(i[0:len(i)-1])
        return len(arr)        