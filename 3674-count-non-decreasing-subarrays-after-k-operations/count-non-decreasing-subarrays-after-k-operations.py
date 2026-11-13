from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        current_cost = 0
        
        # Deque will store indices in decreasing order of their values in nums
        dq = deque()
        
        R = n - 1
        
        # Expand window from right to left (L goes from n-1 down to 0)
        for L in range(n - 1, -1, -1):
            # Pop elements from deque that are smaller than or equal to nums[L]
            # because nums[L] now becomes the controlling max for their intervals.
            last_idx = L
            while dq and nums[dq[0]] <= nums[L]:
                idx = dq.popleft()
                # The popped index controlled elements up to (next deque element index - 1) or R
                next_idx = dq[0] if dq else R + 1
                current_cost += (nums[L] - nums[idx]) * (next_idx - idx)
                last_idx = idx
            
            dq.appendleft(L)
            
            # If current cost exceeds k, shrink window from the right (move R leftward)
            while current_cost > k:
                # The rightmost element R was controlled by the max element at dq[-1]
                current_cost -= (nums[dq[-1]] - nums[R])
                
                # If R reaches the index of the max element itself, remove it from deque
                if dq[-1] == R:
                    dq.pop()
                
                R -= 1
            
            # All valid subarrays starting at L end anywhere between L and R
            ans += (R - L + 1)
            
        return ans