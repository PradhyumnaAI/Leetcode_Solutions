class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        for i in range(0,n):
            if n%(i+1) == 0 :
                summ += nums[i]*nums[i]
            
        return summ


        