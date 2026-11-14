class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minn = float('inf')

        for length in range(l,r+1):
            chunks = [nums[i:i + length] for i in range(0, n - length + 1)]

            for i in range(len(chunks)):
                summ = sum(chunks[i])
                if summ > 0:
                    minn = min(minn, summ)
        
        return minn if minn != float('inf') else -1
