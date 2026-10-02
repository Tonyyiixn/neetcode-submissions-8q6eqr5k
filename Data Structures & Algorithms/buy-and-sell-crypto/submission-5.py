class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = float('inf')
        max_v = 0
        for price in prices:
            min_v = min(min_v,price)
            max_v = max(max_v,price - min_v)
        
        return max_v