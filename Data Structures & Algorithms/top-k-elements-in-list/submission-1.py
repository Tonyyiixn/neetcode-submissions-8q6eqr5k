import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        nums_map = {}
        min_heap = []
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        
        for num,val in nums_map.items():
            heapq.heappush(min_heap,(val,num))

            if len(min_heap)>k:
                heapq.heappop(min_heap)

        
        for pair in min_heap:
            output.append(pair[1])

        return output
