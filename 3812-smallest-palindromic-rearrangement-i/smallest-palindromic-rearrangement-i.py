class Solution:
    def smallestPalindrome(self, s: str) -> str:
        hashmap=defaultdict(int)
        for i in s:
            hashmap[i]+=1
        new=""
        odd=""
        for i in sorted(hashmap):
            if hashmap[i]%2==0:
                new+=i*(hashmap[i]//2)
            else:
                hashmap[i]-=1
                new+=i*(hashmap[i]//2)
                odd=i
        return new+odd+new[::-1]            
