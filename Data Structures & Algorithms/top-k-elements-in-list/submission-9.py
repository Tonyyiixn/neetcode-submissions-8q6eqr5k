class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
        
        sorted_count = sorted(nums_count,key = lambda num:nums_count[num],reverse = True)

        return sorted_count[:k]