class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = {}
        money = 0
        
        def dp(n):
            if n>=len(nums):
                return 0
            
            if n in robbed:
                return robbed[n]
            
            robboth = nums[n] + dp(n + 2)
            skiprob = dp(n+1)

            money = max(robboth,skiprob)
            robbed[n] = money
            return money
        return dp(0)