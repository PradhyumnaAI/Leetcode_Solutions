class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = []
        step = k1 + k2
        
        for i in range(n):
            diff.append(abs(nums1[i] - nums2[i]))

        if step >= sum(diff):
            return 0        

        # Binary search for the minimum possible maximum difference threshold
        left, right = 0, max(diff)
        best_max = right
        
        while left <= right:
            mid = (left + right) // 2
            # Check how many operations are needed to bring all differences > mid down to mid
            ops_needed = sum(max(0, d - mid) for d in diff)
            if ops_needed <= step:
                best_max = mid
                right = mid - 1
            else:
                left = mid + 1

        # 1. Bring all elements down to best_max using operations
        for i in range(n):
            if diff[i] > best_max:
                step -= (diff[i] - best_max)
                diff[i] = best_max

        # 2. Distribute any leftover budget (step) of 1s among elements that are equal to best_max
        for i in range(n):
            if step > 0 and diff[i] == best_max:
                diff[i] -= 1
                step -= 1

        # 3. Calculate final sum of squares
        return sum(d * d for d in diff)