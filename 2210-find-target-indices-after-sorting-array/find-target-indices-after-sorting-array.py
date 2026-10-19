class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [idx for idx, value in enumerate(nums) if value == target]