class Solution:

  def minInsertions(self, s: str) -> int:
    insertions = 0
    open_count = 0
    i = 0
    n = len(s)

    while i < n:
      if s[i] == "(":
        open_count += 1
        i += 1
      else:
        # Check if we have two consecutive closing brackets: '))'
        if i + 1 < n and s[i + 1] == ")":
          # Found '))'
          i += 2
        else:
          # Found single ')', need 1 more ')' inserted
          insertions += 1
          i += 1

        # Now match with an open '(' if available
        if open_count > 0:
          open_count -= 1
        else:
          # No open '(' available, so we must insert 1 '('
          insertions += 1

    # Each remaining unmatched '(' needs 2 closing ')'
    return insertions + (2 * open_count)