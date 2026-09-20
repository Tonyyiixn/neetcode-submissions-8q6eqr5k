class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_v = 0
        for p in prices:
            min_price = min(min_price, p)
            max_v = max(max_v, p - min_price)
        return max_v
