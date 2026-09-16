class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
        
         # sort the numbers (keys) by their count (values), highest first
        sorted_nums = sorted(dic, key=lambda num: dic[num], reverse=True)

        return sorted_nums[:k]

