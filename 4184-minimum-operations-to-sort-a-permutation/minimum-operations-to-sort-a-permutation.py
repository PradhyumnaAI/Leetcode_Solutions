class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        
        def check(step: int) -> bool:
            # Check if the sequence forms a valid cyclic shift with the given step direction (+1 or -1)
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True

        ans = float('inf')
        
        # Path 1: Increasing cyclic order (step = +1)
        if check(1):
            ans = min(ans, zero)            # Direct left rotations
            ans = min(ans, n - zero + 2)    # Reverse + rotate + reverse
            
        # Path 2: Decreasing cyclic order (step = -1)
        if check(-1):
            ans = min(ans, zero + 2)        # Rotate + reverse
            ans = min(ans, n - zero)        # Reverse + rotate
            
        return ans if ans != float('inf') else -1