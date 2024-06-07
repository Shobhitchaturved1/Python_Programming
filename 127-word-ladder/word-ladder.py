class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neigh=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:    
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                neigh[pattern].append(word)
        q=deque([beginWord])
        visit=set([beginWord])
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:] 
                    for neiWord in neigh[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res+=1
        return 0                       
