class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        has_odd=0
        ans=0
        for i in count:
            if count[i]%2!=0:
                ans+=count[i]-1
                has_odd=1
            else:
                ans+=count[i]
        if has_odd:
            return ans+1
        return ans            