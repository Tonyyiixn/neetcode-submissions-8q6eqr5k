class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def f(i):
            if i<= 2:
                return i
            
            if i not in memo:
                memo[i] = f(i-1) + f(i-2)
            
            return memo[i]
        
        return f(n)