class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dic = defaultdict(int)
        for num in nums:
            num_dic[num] += 1
        
        new_list = sorted(num_dic,key= lambda num:num_dic[num],reverse = True)

        return new_list[:k]