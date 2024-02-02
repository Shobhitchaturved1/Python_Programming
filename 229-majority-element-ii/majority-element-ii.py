class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=count2=0
        candidate1=candidate2=0
        for num in nums:
            if count1==0 and num!=candidate2:
                count1=1
                candidate1=num
            elif count2==0 and num!=candidate1:
                count2=1
                candidate2=num
            elif candidate1==num:
                count1+=1
            elif candidate2==num:
                count2+=1
            else:
                count1-=1
                count2-=1
        threshold=len(nums)//3
        res=[]
        count1=count2=0
        for num in nums:
            if candidate1==num:
                count1+=1
            elif candidate2==num:
                count2+=1
        if count1>threshold:
            res.append(candidate1)
        if count2>threshold:
            res.append(candidate2)
        return res                    