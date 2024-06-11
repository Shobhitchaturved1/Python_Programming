class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:return max(nums)
        first=nums[:len(nums)-1]
        second=nums[1:]
        first.append(0)
        second.append(0)
        for i in range(len(first)-3,-1,-1):
            first[i]=max(first[i]+first[i+2],first[i+1])
        cost=max(first[0],first[1])
        for i in range(len(second)-3,-1,-1):
            second[i]=max(second[i]+second[i+2],second[i+1])
        return max(cost,second[0],second[1])        