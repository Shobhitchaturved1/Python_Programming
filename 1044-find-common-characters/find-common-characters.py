class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_size=len(words)
        res=[]
        common_char=Counter(words[0])
        for i in range(1,word_size):
            cur_char=Counter(words[i])
            for letter in common_char.keys():
                common_char[letter]=min(common_char[letter],cur_char[letter])
        for letter,count in common_char.items():
            for _ in range(count):
                res.append(letter)
        return res                
