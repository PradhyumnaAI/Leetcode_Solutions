from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        
        # Count the frequency of each set bit across all numbers
        for num in nums:
            for j in range(31):
                if (num >> j) & 1:
                    bit_counts[j] += 1
                    
        # Construct the k largest possible numbers greedily
        chosen_nums = [0] * k
        for i in range(k):
            current_val = 0
            for j in range(31):
                if bit_counts[j] > 0:
                    current_val |= (1 << j)
                    bit_counts[j] -= 1
            chosen_nums[i] = current_val
            
        # Calculate the sum of squares modulo 10^9 + 7
        total_sum = 0
        for num in chosen_nums:
            total_sum = (total_sum + num * num) % MOD
            
        Info = total_sum
        return Info