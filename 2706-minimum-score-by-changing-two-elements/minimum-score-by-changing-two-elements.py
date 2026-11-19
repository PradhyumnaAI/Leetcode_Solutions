class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3:
            return 0
        nums.sort()
        
        diff1 = (nums[n-1]-nums[2])
        diff2 = (nums[n-3]-nums[0])
        diff3 = (nums[n-2]- nums[1])

        return min(diff1,diff2,diff3)


        