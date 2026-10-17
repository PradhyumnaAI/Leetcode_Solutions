from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        dict1 = []
        n = len(nums)
        
        for i in range(n):
            summ = 0
            temp = nums[i]
            
            
            while temp > 0:
                summ += temp % 10
                temp //= 10
                
            dict1.append((summ, nums[i], i))

        
        dict1.sort()

        swaps = 0
        current = list(dict1)
        
        for i in range(n):
            while current[i][2] != i:
                target_idx = current[i][2]
                current[i], current[target_idx] = current[target_idx], current[i]
                swaps += 1

        return swaps