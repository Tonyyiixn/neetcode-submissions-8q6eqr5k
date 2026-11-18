class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n + 0) * (n+1) // 2 - sum(nums)