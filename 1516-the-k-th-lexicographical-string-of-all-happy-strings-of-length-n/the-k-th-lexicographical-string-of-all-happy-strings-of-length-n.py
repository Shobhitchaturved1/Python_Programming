class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        left,right = 1,3*2**(n-1)
        choices = 'abc'
        res = []
        for i in range(n):
            partition_size = (right-left+1)//len(choices)
            for ch in choices:
                if left<=k<left+partition_size:
                    res.append(ch)
                    right = left+partition_size - 1
                    choices = 'abc'.replace(ch,'')
                    break
                left+=partition_size
        return ''.join(res)