class Solution:
    def rob(self, nums: List[int]) -> int:
        max_value = 0
        memo = {}
        def dp(n):
            if n < 0:
                return 0
            
            if n not in memo:
                memo[n] = max(nums[n]+dp(n - 2) , dp(n-1))
            
            return memo[n]
        
        return dp(len(nums)-1)