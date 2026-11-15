class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd_count = 0 
        even_count=1
        ans = 0
        MOD = 10**9 + 7
        current_sum = 0
        for i in arr : 
            current_sum+=i
            if current_sum %2 != 0:
                ans = (ans + even_count)%MOD
                odd_count+=1
            else:
                ans = (ans + odd_count)%MOD
                even_count+=1
        return ans





        