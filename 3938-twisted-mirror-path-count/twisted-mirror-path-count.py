class Solution:

  def uniquePaths(self, grid: List[List[int]]) -> int:
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])

    # Memoization cache for jump targets to avoid redundant calculations
    # jump[i][j][0] -> jump if moving Right from (i, j)
    # jump[i][j][1] -> jump if moving Down from (i, j)
    jump = [[None, None] for _ in range(m * n)]

    def get_jump(r, c, direction):
      # direction: 0 for Right, 1 for Down
      idx = r * n + c
      if jump[idx][direction] is not None:
        return jump[idx][direction]

      curr_r, curr_c = r, c
      curr_dir = direction  # 0: Right, 1: Down

      while True:
        if curr_dir == 0:
          nxt_r, nxt_c = curr_r, curr_c + 1
        else:
          nxt_r, nxt_c = curr_r + 1, curr_c

        # Check bounds
        if not (0 <= nxt_r < m and 0 <= nxt_c < n):
          jump[idx][direction] = -1  # Invalid / Out of bounds
          return -1

        # If it's a mirror, reflect immediately
        if grid[nxt_r][nxt_c] == 1:
          if curr_dir == 0:
            curr_dir = 1  # Turn down
          else:
            curr_dir = 0  # Turn right
          curr_r, curr_c = nxt_r, nxt_c
        else:
          # Lands on a valid empty cell
          jump[idx][direction] = (nxt_r, nxt_c)
          return (nxt_r, nxt_c)

    # DP table initialized to 0
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
      for j in range(n):
        if dp[i][j] == 0:
          if (i, j) != (0, 0):
            continue

        ways = dp[i][j]

        # Try moving Right (direction 0)
        target_right = get_jump(i, j, 0)
        if target_right != -1:
          tr, tc = target_right
          dp[tr][tc] = (dp[tr][tc] + ways) % MOD

        # Try moving Down (direction 1)
        target_down = get_jump(i, j, 1)
        if target_down != -1:
          tr, tc = target_down
          dp[tr][tc] = (dp[tr][tc] + ways) % MOD

    return dp[m - 1][n - 1]