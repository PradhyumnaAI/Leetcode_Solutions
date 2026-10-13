class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squared_nums = sorted([x**2 for x in nums])
        
        n = len(squared_nums)
        sum1 = 0
        sum2 = 0
        
        # The first n // 2 elements are the smallest, so they go to sum2 (subtracted)
        # The remaining elements go to sum1 (added)
        m = n // 2
        for i in range(n - 1, -1, -1):
            if i >= m:
                sum1 += squared_nums[i]
            else:
                sum2 += squared_nums[i]
                
        return sum1 - sum2