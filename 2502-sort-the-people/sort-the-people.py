class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap=defaultdict(int)
        for x,y in zip(names,heights):
            hashmap[y]=x
        return [hashmap[i] for i in reversed(sorted(hashmap.keys()))]