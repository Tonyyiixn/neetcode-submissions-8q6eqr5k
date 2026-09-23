class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals_set = {}
        for index, val  in enumerate(nums):
            if (target - val) in vals_set:
                return [vals_set[target-val],index]
            vals_set[val] = index
        
        return []