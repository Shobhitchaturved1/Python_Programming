class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count=0
        if k>=len(arr):
            return max(arr)
        i=0 
        c=arr[0]   
        while(i<len(arr)-1):
            if c>arr[i+1] or arr[i]>arr[i+1]:
                count+=1
                if(count==k):
                    return arr[i]
                temp=arr[i+1]
                arr.remove(arr[i+1])
                arr+=[temp]
            else:
                c=arr[i+1]
                count=1 
                if(count==k):
                    return arr[i+1]
                temp=arr[i]
                arr.remove(arr[i])
                arr+=[temp]       
