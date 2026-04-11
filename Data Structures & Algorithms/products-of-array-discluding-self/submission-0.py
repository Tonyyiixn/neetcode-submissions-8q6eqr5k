class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # 1. Build the left products inside the output array
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
            
        # 2. Multiply by the right products, moving backwards
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
            
        return output