class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        def quickselect(arr, k):
            if len(arr) == 1:
                return arr[0]
            
            pivot = arr[len(arr) // 2]
            
            lows = [x for x in arr if x < pivot]
            highs = [x for x in arr if x > pivot]
            pivots = [x for x in arr if x == pivot]
            
            if k < len(lows):
                return quickselect(lows, k)
            elif k < len(lows) + len(pivots):
                return pivots[0]
            else:
                return quickselect(highs, k - len(lows) - len(pivots))

        median_val = quickselect(nums, len(nums) // 2)
        return sum(abs(num - median_val) for num in nums)