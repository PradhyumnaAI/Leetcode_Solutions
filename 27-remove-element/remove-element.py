class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Pointer for next valid element position
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        