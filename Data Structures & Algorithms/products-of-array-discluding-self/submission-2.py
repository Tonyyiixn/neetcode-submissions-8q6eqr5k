class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
       
        
        temp =  1
        for j in range(len(nums)):
            left[j] = temp
            temp = nums[j] * temp #1 1 * 1 1 *2  2* 4 1 1 2 8
        
        temp = 1
        for k in range(len(nums)-1 , -1 , -1):
            right[k] = left[k] * temp 
            temp = nums[k] * temp # 1 1 * 6 6 * 4 24 * 2
        
        return right