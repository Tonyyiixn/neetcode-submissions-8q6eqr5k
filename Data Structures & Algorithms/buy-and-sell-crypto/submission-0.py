class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        val = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                val = max(prices[r] - prices[l],val)
                r += 1
            else:
                l = r
                r += 1
        
        return val