class Solution:
    def canJump(self, nums: List[int]) -> bool:
        further = 0
        for i in range(len(nums)):
            if i > further:
                return False
            further = max(further,i+nums[i])
        return True