class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        start = 0
        while nums[start] != 0:
            start += 1
            
        asc = True
        desc = True
        
        for i in range(1, n):
            value = nums[(start + i) % n]
            
            if value != i:
                asc = False
            if value != n - i:
                desc = False
                
            if not asc and not desc:
                return -1
                
        if asc:
            return min(start, n - start + 2)
            
        return min(n - start, start + 2)