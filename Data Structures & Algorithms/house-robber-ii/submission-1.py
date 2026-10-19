class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def f(houses):
            curr = 0
            prev = 0
            for money in houses:
                max_value = max(curr,prev+money)
                prev = curr
                curr = max_value
            return curr
        
        return max(f(nums[1:]),f(nums[:-1]))