class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(arr):
            curr = 0
            prev = 0
            for num in arr:
                tmp = curr
                curr = max(curr,prev+num)
                prev = tmp
            return curr
        
        return max(dp(nums[1:]),dp(nums[:-1]))