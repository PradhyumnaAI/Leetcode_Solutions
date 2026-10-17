from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        dict1 = []
        n = len(nums)
        
        for i in range(n):
            summ = 0
            string1 = str(nums[i])
            for j in range(len(string1)):
                summ += int(string1[j])
            dict1.append((summ, nums[i], i))

        # Sort based on digit sum, then by value (tie-breaker)
        dict1.sort(key=lambda x: (x[0], x[1]))

        swaps = 0
        # Create a mutable copy of the list of items to simulate actual swaps
        current = list(dict1)
        
        for i in range(n):
            # Keep swapping elements into their correct sorted position
            while current[i][2] != i:
                target_idx = current[i][2]
                # Swap elements
                current[i], current[target_idx] = current[target_idx], current[i]
                swaps += 1

        return swaps