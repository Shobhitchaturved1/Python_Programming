class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        def solve(arr):
            for i in range(len(arr)-3,-1,-1):
                arr[i]=max(arr[i+1],arr[i]+arr[i+2])
            return max(arr[0],arr[1])
        return max(solve(nums[1:]+[0]),solve(nums[:-1]+[0]))        