class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start,new_end = newInterval
        res = []
        for i,(start,end) in enumerate(intervals):
            if new_end < start:
                res.append([new_start,new_end])
                return res + intervals[i:]
            elif new_start > end:
                res.append([start,end])
            else:
                new_start = min(start,new_start)
                new_end = max(end,new_end)
        res.append([new_start,new_end])

        return res