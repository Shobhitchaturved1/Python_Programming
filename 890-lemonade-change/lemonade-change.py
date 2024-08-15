class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5=count10=count20=0
        for i in bills:
            if i==5:
                count5+=1
            elif i==10:
                if count5:
                    count5-=1
                    count10+=1
                else:
                    return False
            else:
                if count5 and count10:
                    count5-=1
                    count10-=1
                    count20+=1
                elif count5>=3:
                    count5-=3
                    count20+=1    
                else:
                    return False
        return True                                