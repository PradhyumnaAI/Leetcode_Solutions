class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        minn = nums[0]
        n = len(nums)
        summ =0
        
        for i in range(n-1,-1,-1):
            summ += nums[i]-minn
        
        return summ