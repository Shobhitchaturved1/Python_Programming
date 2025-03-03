class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)

        def isPalindrome(i,j):

            return s[i:j+1] == s[i:j+1][::-1]
        
        dp = [-1 for _ in range(n)]
        #palindrom_dp = [[-1 for _ in range(n)] for _ in range(n)]
        def f(i):
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            _min = float('inf')

            for idx in range(i,n):
                if isPalindrome(i,idx):
                    cuts = 1 + f(idx+1)
                    _min = min(_min,cuts)
            dp[i] = _min
            return _min
        
        return f(0)-1