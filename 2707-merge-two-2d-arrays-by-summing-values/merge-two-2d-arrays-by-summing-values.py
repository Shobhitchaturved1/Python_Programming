class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i,j=0,0
        ans=[]
        while i<len(nums1) and j<len(nums2):
            a,b=nums1[i][0],nums1[i][1]
            x,y=nums2[j][0],nums2[j][1]
            if a==x:
                ans.append([a,b+y])
                i+=1
                j+=1
            elif a<x:
                ans.append([a,b])
                i+=1
            else:
                ans.append([x,y])
                j+=1
        if i:
            ans=ans+nums1[i:]
        if j:
            ans=ans+nums2[j:]
        return ans                            

        