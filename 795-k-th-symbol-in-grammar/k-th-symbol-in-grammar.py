class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        left=1
        right=2**(n-1)
        cur=0
        for _ in range(n):
            mid=(left+right)//2
            if k<=mid:
                right=mid
            else:
                left=mid+1
                cur=0 if cur else 1
        return cur            