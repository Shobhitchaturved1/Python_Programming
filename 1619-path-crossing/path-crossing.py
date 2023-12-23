class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hash_map=defaultdict(int)
        x=0
        y=0
        hash_map[(x,y)]=1
        for i in path:
            if i=="N":
                y+=1
            elif i=="S":
                y-=1
            elif i=="E":
                x+=1
            else:
                x-=1
            hash_map[(x,y)]+=1            
            if hash_map[(x,y)]>1:
                return True
        return False        


        