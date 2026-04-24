class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(n:int) -> int:
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            if n in memo:
                return memo[n]
            operand1 = dp(n-1)
            operand2 = dp(n-2)

            result = operand1 + operand2

            memo[n] = result

            return result
        
        return dp(n)