class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=defaultdict(list)
        for cour,pre in prerequisites:
            preMap[cour].append(pre)
        visit=set()    
        def dfs(i):
            if i in visit:
                return False
            if preMap[i]==[]:
                return True
            visit.add(i)
            for pre in preMap[i]:
                if not dfs(pre):return False
            visit.remove(i)
            preMap[i]=[]
            return True                       
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True        