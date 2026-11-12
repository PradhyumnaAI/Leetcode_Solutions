class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # 1. Overlapping requirement satisfied by the cheaper option between Type 3 or (Type 1 + Type 2)
        common_units = min(need1, need2)
        common_cost = min(costBoth, cost1 + cost2)
        total_cost = common_units * common_cost
        
        # 2. Remaining requirements after fulfilling the common units
        need1 -= common_units
        need2 -= common_units
        
        # 3. Fulfill any leftover units for requirement 1
        if need1 > 0:
            total_cost += need1 * min(cost1, costBoth)
            
        # 4. Fulfill any leftover units for requirement 2
        if need2 > 0:
            total_cost += need2 * min(cost2, costBoth)
            
        return total_cost