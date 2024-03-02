class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        i=0
        j=len(nums)-1
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                arr.append(nums[i]*nums[i])
                #print(arr)
                i+=1
            else:
                arr.append(nums[j]*nums[j])
                j-=1
        return arr[::-1]               