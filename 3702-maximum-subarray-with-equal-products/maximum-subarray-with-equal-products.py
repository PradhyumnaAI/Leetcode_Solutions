class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def find_gcd(arr:List[int]) -> int:
            smallest = min(arr)
            # idx = 1
            # while idx< len(arr):
            #     if arr[idx]<smallest:
            #         smallest = arr[idx]
            #     idx+=1
            
            candidate = smallest
            while candidate>=1:
                divides_all = True
                for val in arr :
                    if val%candidate!=0:
                        divides_all = False
                        break
                if divides_all:
                    return candidate
                candidate-=1
            return 1
        def find_lcm (arr:List[int],upper_bound:int)->int:
            largest = max(arr)
            # idx = 1
            # while idx < len(arr):
            #     if arr[idx] > largest:
            #         largest = arr[idx]
            #     idx += 1

            multiple = largest
            while multiple <= upper_bound:
                all_divide_it = True
                for val in arr:
                    if multiple % val != 0:
                        all_divide_it = False
                        break
                if all_divide_it:
                    return multiple
                multiple += largest
            return upper_bound

        def find_prod(arr:List[int])->int:
            total = 1
            for val in arr:
                total = total * val
            return total 
            
        max_len = 0 
        n = len(nums)
        i = 0 
        while i<n:
            j=i 
            while j<n:
                sub = nums[i:j+1]
                prod = find_prod(sub)
                gcd = find_gcd(sub)
                lcm = find_lcm(sub,prod)

                if prod == gcd*lcm:
                    length = j-i+1
                    if length >max_len:
                        max_len = length
                j+=1
            i+=1
        return max_len

