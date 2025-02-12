class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_count=defaultdict(list)
        for i in nums:
            num=[int(j) for j in str(i)]
            digit_count[sum(num)].append(i)
        ans=-1
        print(digit_count)
        for i in digit_count:
            if len(digit_count[i])<2:
                continue
            largest_two = heapq.nlargest(2, digit_count[i])
            ans = max(ans, largest_two[0] + largest_two[1])
        return ans     