class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit=set()
        visit.add(0)
        q=rooms[0]
        while q:
            idx=q.pop()
            if idx not in visit:
                visit.add(idx)
                for i in rooms[idx]:
                    if i not in visit:
                        q.append(i)
        return len(visit)==len(rooms)                
