class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        #product of left
        tmp = 1
        for i in range(len(nums)):
            left[i] = tmp 
            tmp = tmp * nums[i]
        
        #product of right
        tmp = 1
        for j in range(len(nums)-1,-1,-1):
            left[j] = tmp * left[j]
            tmp = tmp * nums[j]
        
        return left
        
        