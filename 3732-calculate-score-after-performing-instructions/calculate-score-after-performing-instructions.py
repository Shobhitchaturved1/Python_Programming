class Solution:
    def calculateScore(self, ins: List[str], values: List[int]) -> int:
        score=0
        i=0
        re=set()
        while 0<=i<len(values):
            if i in re:
                break
            if ins[i]=="add":
                score+=values[i]
                re.add(i)
                i+=1
            else:
                re.add(i)
                i+=values[i]
        return score            