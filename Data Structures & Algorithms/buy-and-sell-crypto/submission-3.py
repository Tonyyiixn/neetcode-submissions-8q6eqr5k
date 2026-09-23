class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = float('inf')
        max_v = 0
        for price in prices:
            min_ = min(min_, price)
            max_v = max(max_v,price - min_)
        
        return max_v