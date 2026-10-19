class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def f(i):
            if i < 0:
                return 0
            if i not in memo:
                memo[i] = max(f(i-1),f(i-2)+nums[i])
            return memo[i]
        
        return f(len(nums)-1)