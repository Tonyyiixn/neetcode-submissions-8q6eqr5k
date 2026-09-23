class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dic  = defaultdict(int)
        for num in nums:
            nums_dic[num] += 1
        
        nums_dic = sorted(nums_dic,key= lambda num: nums_dic[num],reverse =  True)

        return nums_dic[:k]