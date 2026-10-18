class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack1 = nums + nums
        output = []
        n = len(nums)
        
        

        for idx,i in enumerate(nums):
            for j in stack1[idx+1:idx+n]:
                if j > i :
                    output.append(j)
                    break
            else:
                output.append(-1)
        return output          
        