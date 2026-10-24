class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(arr):
            prev1, prev2 = 0,0 # dp(i-1),dp(i-2)
            for num in arr:
                prev2 , prev1 = prev1, max(prev1,prev2+num)
            return prev1

        return max(dp(nums[:-1]),dp(nums[1:]))