class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        
        sorted_num_dict = sorted(nums_dict,key = lambda num:nums_dict[num],reverse = True)

        return sorted_num_dict[:k]