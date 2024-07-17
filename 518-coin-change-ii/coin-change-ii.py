class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row = [0] * (amount + 1)
        row[0]=1
        for i in reversed(coins):
            newrow=row
            for j in range(1,len(row)):
                if j-i>=0:
                    newrow[j]+=newrow[j-i]
            row=newrow
            
            #print(row)
        return row[-1]            
