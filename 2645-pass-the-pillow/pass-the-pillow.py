class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full_round=time//(n-1)
        extra_time=time%(n-1)
        if full_round%2==0:
            return extra_time+1
        else:
            return n-extra_time    