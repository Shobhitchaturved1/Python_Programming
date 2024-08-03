class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        map1,map2=defaultdict(int),defaultdict(int)
        if len(arr)!=len(target):return False
        for i in range(len(arr)):
            map1[arr[i]]+=1
            map2[target[i]]+=1
        return map1==map2    