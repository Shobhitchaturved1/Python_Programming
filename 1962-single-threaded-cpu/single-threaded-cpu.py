class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        res=[]
        minHeap=[]
        time=tasks[0][0]
        cur_task_index=0
        while len(res)<len(tasks):
            while(cur_task_index<len(tasks) and (tasks[cur_task_index][0]<=time)):
                heapq.heappush(minHeap,(tasks[cur_task_index][1],tasks[cur_task_index][2]))
                cur_task_index+=1
            if minHeap:
                diff,idx=heapq.heappop(minHeap)
                time+=diff 
                res.append(idx)
            elif cur_task_index<len(tasks):
                time=tasks[cur_task_index][0]       
        return res        