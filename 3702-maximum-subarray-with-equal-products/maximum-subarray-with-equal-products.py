class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def custom_gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        def lcm_of_two(a: int, b: int) -> int:
            if a == 0 or b == 0:
                return 0
            return abs(a * b) // custom_gcd(a, b)

        def lcm_of_list(arr: List[int]) -> int:
            if not arr:
                return 0
            result = arr[0]
            idx = 1
            while idx < len(arr):
                result = lcm_of_two(result, arr[idx])
                idx += 1
            return result

        def gcd_of_list(numbers: List[int]) -> int:
            if not numbers:
                return 0
            result = numbers[0]
            idx = 1
            while idx < len(numbers):
                result = custom_gcd(result, numbers[idx])
                if result == 1:
                    return 1
                idx += 1
            return result

        def prod_of_list(arr: List[int]) -> int:
            prod_val = 1
            for val in arr:
                prod_val = prod_val * val
            return prod_val

        max_len = 0
        n = len(nums)

        i = 0
        while i < n:
            j = i
            while j < n:
                sub = nums[i : j + 1]
                lcm_val = lcm_of_list(sub)
                gcd_val = gcd_of_list(sub)
                prod_val = prod_of_list(sub)

                if prod_val == lcm_val * gcd_val:
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                j += 1
            i += 1

        return max_len