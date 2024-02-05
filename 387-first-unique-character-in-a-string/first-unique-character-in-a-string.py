class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps=defaultdict(int)
        for i in s:
            maps[i]+=1
        for i in range(len(s)):
            if maps[s[i]]==1:
                return i
        return -1            