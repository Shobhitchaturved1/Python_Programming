class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence=list(sentence.split(" "))
        for i in range(len(sentence)):
            for j in dictionary:
                word=sentence[i]
                length=len(j)
                if word[:length]==j and length<len(word):
                    sentence[i]=j
        return " ".join(sentence)            