class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute proper divisors for each length from 1 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # Helper to find min changes to make s[i..j] a palindrome for a fixed step d and offset
        def palindrome_changes(i, j, d):
            changes = 0
            for start in range(d):
                left = i + start
                right = i + (j - i) // d * d + start
                # Move within the group defined by step d
                while left < right:
                    if s[left] != s[right]:
                        changes += 1
                    left += d
                    right -= d
            return changes

        # Precompute cost[i][j]: min changes to make substring s[i..j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_c = float('inf')
                for d in divisors[length]:
                    min_c = min(min_c, palindrome_changes(i, j, d))
                cost[i][j] = min_c

        # DP table: dp[i][c] = min changes to partition s[i..n-1] into c parts
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0

        for idx in range(n - 1, -1, -1):
            for c in range(1, k + 1):
                # We need at least enough characters remaining to form c parts of length >= 2
                if n - idx < 2 * c:
                    continue
                res = float('inf')
                # Try all possible cut points x for the first part s[idx..x]
                for x in range(idx + 1, n - 2 * (c - 1) ):
                    res = min(res, cost[idx][x] + dp[x + 1][c - 1])
                dp[idx][c] = res

        return dp[0][k]