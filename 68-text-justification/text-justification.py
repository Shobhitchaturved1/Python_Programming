class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        s=[]
        length=0
        i=0
        while i<len(words):
            #length + 1 space in between words + new word length
            if length + len(s) + len(words[i]) >maxWidth:
                #need to add extra space in between
                extra_space=maxWidth-length
                #because of divide by zero error
                spaces=extra_space//max(1,len(s)-1)
                remainder=extra_space%max(1,len(s)-1)
                #if only 1 word in line
                for j in range(max(1,len(s)-1)):
                    s[j]=s[j]+ " "*spaces
                    if remainder:
                        s[j]+=" "
                        remainder-=1
                res.append("".join(s))
                s=[]
                length=0        
            s.append(words[i])
            length+=len(words[i])
            i+=1   
        last_line=" ".join(s)
        trail_space=maxWidth-len(last_line)     
        res.append(last_line+" "*trail_space)
        return res