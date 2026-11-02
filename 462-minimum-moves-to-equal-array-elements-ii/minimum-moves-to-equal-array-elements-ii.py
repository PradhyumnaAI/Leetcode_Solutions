class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        element = nums[n//2]
        summ = 0
        for i in range(n):
            summ+= abs(element - nums[i])

        return summ
        