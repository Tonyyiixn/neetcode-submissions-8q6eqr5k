class Solution:
    def rob(self, nums: List[int]) -> int:
        # prev represents max money up to 2 houses ago
        # curr represents max money up to 1 house ago
        prev = 0
        curr = 0
        
        for money_in_house in nums:
            # We either rob this house (money_in_house + prev)
            # OR we skip it and keep what we had (curr)
            next_max = max(money_in_house + prev, curr)
            
            # Leapfrog forward for the next house
            prev = curr
            curr = next_max
            
        return curr