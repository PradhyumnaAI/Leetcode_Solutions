class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Fenwick tree for range updates & range queries (Linear counts)
        tree_val = [0] * (n + 2)
        tree_idx = [0] * (n + 2)
        
        def add(i, val):
            # 1-based indexing for BIT
            i += 1
            curr_val = val
            curr_idx = (i - 1) * val
            while i <= n:
                tree_val[i] = (tree_val[i] + curr_val) % MOD
                tree_idx[i] = (tree_idx[i] + curr_idx) % MOD
                i += i & (-i)
                
        def range_add(l, r, val):
            add(l, val)
            add(r + 1, -val)
            
        def prefix_sum(i):
            i += 1
            res_val = 0
            res_idx = 0
            orig_i = i
            while i > 0:
                res_val = (res_val + tree_val[i]) % MOD
                res_idx = (res_idx + tree_idx[i]) % MOD
                i -= i & (-i)
            return (orig_i * res_val - res_idx) % MOD
            
        def range_sum(l, r):
            if l > r:
                return 0
            res = prefix_sum(r)
            if l > 0:
                res = (res - prefix_sum(l - 1) + MOD) % MOD
            return res

        last_occurrence = {}
        ans = 0
        current_sum_squares = 0
        
        for j in range(n):
            x = nums[j]
            last_pos = last_occurrence.get(x, -1)
            
            l, r = last_pos + 1, j
            range_len = r - l + 1
            
            # Query sum of counts in range [l, r]
            linear_sum = range_sum(l, r)
            
            # Delta for squares = 2 * linear_sum + range_len
            delta = (2 * linear_sum + range_len) % MOD
            current_sum_squares = (current_sum_squares + delta) % MOD
            
            # Range update: add 1 to range [l, r]
            range_add(l, r, 1)
            
            last_occurrence[x] = j
            ans = (ans + current_sum_squares) % MOD
            
        return ans