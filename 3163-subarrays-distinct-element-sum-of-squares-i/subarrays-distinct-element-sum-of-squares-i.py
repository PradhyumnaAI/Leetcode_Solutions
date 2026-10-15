class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Outer loop for the starting index of the subarray
        for i in range(n):
            seen = set()
            # Inner loop for the ending index of the subarray
            for j in range(i, n):
                seen.add(nums[j])
                # Add the square of the distinct count (size of the set)
                total_sum += len(seen) ** 2
                
        return total_sum