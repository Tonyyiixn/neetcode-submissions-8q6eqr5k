class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = float('inf')
        max_v = 0
        for p in prices:
            min_v = min(min_v,p)
            max_v = max(max_v,p - min_v)
        
        return max_v