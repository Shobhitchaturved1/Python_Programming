class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        preMap={i:[] for i in range(numCourses)}
        visit=set()
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        def dfs(course):
            if course in visit:
                return False
            if preMap[course]==[] and course not in ans:
                ans.append(course)
                return True
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre):return []
            visit.remove(course)
            preMap[course]=[]
            if course not in ans:
                ans.append(course)
            return True
        for crs in range(numCourses):
            if not dfs(crs):return []
            if crs not in ans:
                ans.append(crs)
        return ans        

