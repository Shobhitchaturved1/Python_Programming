class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l=0
        r=len(products)-1
        idx=1
        ans=[]
        while idx<=len(searchWord):
            while products[l][:idx]!=searchWord[:idx]:
                l+=1
                if l>=len(products):
                    ans+=([[]]*(len(searchWord)-idx+1))
                    return ans 
            while products[r][:idx]!=searchWord[:idx]:
                r-=1    
            idx+=1
            if r-l>=3:
                ans.append(products[l:l+3])
            else:
                ans.append(products[l:r+1])
        return ans                    