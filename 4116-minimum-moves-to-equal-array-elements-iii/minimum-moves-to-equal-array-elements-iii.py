class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx = max(nums)
        n = len(nums)
        count = 0
        for i in range(n):
            count += abs(maxx - nums[i])
        
        return count
