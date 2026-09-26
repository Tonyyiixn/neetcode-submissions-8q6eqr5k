class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_set = {}
        for index,num in enumerate(nums):
            if (target - num) in index_set:
                return [index_set[target - num],index]
            index_set[num] = index
       