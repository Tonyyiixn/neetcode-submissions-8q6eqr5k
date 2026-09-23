class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_Ana  = defaultdict(list)
        for s in strs:
            group_Ana[tuple(sorted(s))].append(s)
        
        return list(group_Ana.values())