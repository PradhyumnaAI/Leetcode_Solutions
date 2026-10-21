class Solution:
  def minOperations(self, s: str) -> int:
    s1 = "".join(sorted(s))
    n = len(s)

    if s1 == s:
      return 0
    if n == 2:
      return -1

    mn, mx = min(s), max(s)
    if s[0] == mn or s[-1] == mx:
      return 1

    has_min_prefix = mn in s[:-1]
    has_max_suffix = mx in s[1:]   # s, not s1

    if not has_min_prefix and not has_max_suffix:
      return 3
    return 2