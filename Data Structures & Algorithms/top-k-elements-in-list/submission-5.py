class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 1

        sorted_res = sorted(res,key=res.get, reverse= True)
        return sorted_res[:k]
