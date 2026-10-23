class Solution:

  def sortPermutation(self, nums: List[int]) -> int:
    n = len(nums)
    k = -1  # -1 acts as an identity mask for bitwise AND

    for i in range(n):
      if i != nums[i]:
        if k == -1:
          k = nums[i]
        else:
          k &= nums[i]

    return max(k, 0)