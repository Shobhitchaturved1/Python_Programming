class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #store all prime from left to right
        primes=[]
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        nums1,nums2=-1,-1
        ans=float("inf")            
        for i in range(left,right+1):
            if isprime(i):
                primes.append(i)
            if len(primes)==2:
                if ans>primes[1]-primes[0]:
                    ans=primes[1]-primes[0]
                    nums1=primes[0]
                    nums2=primes[1]
                if ans==2:break
                primes.pop(0)
        return [nums1,nums2]        
            