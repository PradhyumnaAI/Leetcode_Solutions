class Solution:

  def minOperations(self, s: str) -> int:
    s1 = "".join(sorted(s))
    n = len(s)

    if s1 == s:
      return 0

    if n == 2:
      return -1

    # 1 operation if min is at the start OR max is at the end (and it's not already sorted)
    if (s[0] == min(s) and s != s1) or (s[-1] == max(s) and s != s1):
      return 1

    # 3 operations if no minimum exists in any proper prefix and no maximum in any proper suffix
    mn = min(s)
    mx = max(s)
    has_min_prefix = mn in s[:-1]
    has_max_suffix = mx in s[1:]

    if not has_min_prefix and not has_max_suffix:
      return 3

    return 2