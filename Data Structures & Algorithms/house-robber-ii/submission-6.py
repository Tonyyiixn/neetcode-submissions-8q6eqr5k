class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(arr):
            prev,curr = 0,0
            for num in arr:
                max_value = max(curr,prev+num)
                prev = curr
                curr = max_value
            
            return curr
        
        return max(dp(nums[:-1]),dp(nums[1:]))