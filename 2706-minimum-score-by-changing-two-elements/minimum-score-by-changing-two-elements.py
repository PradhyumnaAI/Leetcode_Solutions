class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        diff1 = abs(nums[n-1]-nums[2])
        diff2 = abs(nums[n-3]-nums[0])
        diff3 = abs(nums[1]- nums[n-2])

        return min(diff1,diff2,diff3)


        