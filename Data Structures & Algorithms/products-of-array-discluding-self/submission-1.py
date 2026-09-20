class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        temp = 1
        for i in range(len(nums)):
            left[i] = temp 
            temp *= nums[i]
            # left: [1, 1 , 2, 8]
        
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            right[i] = left[i] * temp # 1: 8 * 1,  2: 2 * 1 * 6 , 3: 1 * 4 * 6, 4: 1 * 2 * 4 * 6
            temp = temp * nums[i] # 1 * 6 , 1* 6 * 4 , 1* 6 *4 * 2


        return right