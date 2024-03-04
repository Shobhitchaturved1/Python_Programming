class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i=0
        j=len(tokens)-1
        tokens.sort()
        score=0
        res=0
        if len(tokens)==1:
            return 1 if power>=tokens[0] else 0
        while i<j:
            if power>=tokens[i]:
                while power>=tokens[i]:
                    power-=tokens[i]
                    i+=1
                    score+=1
            else:
                res=max(res,score)
                if score>=1:
                    score-=1
                    power+=tokens[j]
                    j-=1
                else:
                    return score    
        return max(res,score)            