class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0=0
        count1=0
        for i in students:
            if i==0:
                count0+=1
            else:
                count1+=1
        for i in range(len(sandwiches)):
            if sandwiches[i]==1 and count1>0:
                count1-=1
            elif sandwiches[i]==0 and count0>0:
                count0-=1
            else:
                return len(sandwiches)-i
        return 0        
                