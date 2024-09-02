class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n=sum(chalk)
        rem=k%n
        for i in range(len(chalk)):
            rem-=chalk[i]
            if rem<0:
                return i
