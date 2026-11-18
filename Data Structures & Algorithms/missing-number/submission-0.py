class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        standard = set(range(n+1))
        for num in nums:
            standard.remove(num)
        return standard.pop()
