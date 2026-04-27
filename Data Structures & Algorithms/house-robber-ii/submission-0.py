class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def tradictional (houses: List[int]) -> int: 
            robbed = {}

            def dp(n:int) -> int:
                if n>=len(houses):
                    return 0
                
                if n in robbed:
                    return robbed[n]
                
                robboth = houses[n] + dp(n+2)
                robskip = dp(n+1)
                
                money = max(robboth,robskip)
             
                robbed[n] = money
                
                return money
        
            return dp(0)
        
        patha = tradictional(nums[:-1])
        pathb = tradictional(nums[1:])

        return max(patha,pathb)