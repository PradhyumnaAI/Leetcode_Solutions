class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Quick feasibility check
        if sum < 0 or sum > num * 9:
            return ""
            
        res = []
        rem_sum = sum
        
        for i in range(num):
            remaining_slots = num - 1 - i
            # Try digits from 9 down to 0
            for d in range(9, -1, -1):
                # Check if picking digit `d` leaves a valid remaining sum
                if rem_sum - d <= remaining_slots * 9 and rem_sum - d >= 0:
                    res.append(str(d))
                    rem_sum -= d
                    break
                    
        return "".join(res)