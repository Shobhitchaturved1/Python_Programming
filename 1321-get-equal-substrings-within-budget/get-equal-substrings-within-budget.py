class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len=0
        start=0
        cur_cost=0
        for i in range(len(s)):
            cur_cost+=abs(ord(s[i])-ord(t[i]))
            while cur_cost>maxCost:
                cur_cost-=abs(ord(s[start])-ord(t[start]))
                start+=1
            max_len=max(max_len,i-start+1)
        return max_len        