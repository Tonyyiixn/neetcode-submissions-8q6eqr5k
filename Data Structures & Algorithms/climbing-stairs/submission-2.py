class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev = 1
        curr = 2
        for _ in range(3,n+1):
            next_step = prev + curr

            prev = curr
            curr = next_step
            

        return curr 