class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=defaultdict(int)
        lose=defaultdict(int)
        arr1=[]
        arr2=[]
        for a,b in matches:
            win[a]+=1
            lose[b]+=1
        for i in win:
            if win[i]>=1 and lose[i]==0:
                arr1+=[i]
        for i in lose:
            if lose[i]==1:
                arr2+=[i]        
        return [sorted(arr1),sorted(arr2)]        
