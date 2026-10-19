class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        output = []
        
        for idx,value in enumerate(nums) :
            if value == target:
                output.append(idx)
        
        return output
