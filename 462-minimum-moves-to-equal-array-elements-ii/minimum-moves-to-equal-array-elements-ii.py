import statistics
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # nums.sort()
        mid_value = statistics.median(nums)
        # median = nums[len(nums) // 2]
        return int(sum(abs(num - mid_value) for num in nums))
        