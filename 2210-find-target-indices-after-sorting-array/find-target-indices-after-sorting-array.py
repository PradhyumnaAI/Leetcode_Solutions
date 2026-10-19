class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums = sorted(nums)
        output = []
        if len(nums)==0:
            return []
        for idx,value in enumerate(nums) :
            if value == target:
                output.append(idx)
        if len(output)==0:
            return []
        return output
