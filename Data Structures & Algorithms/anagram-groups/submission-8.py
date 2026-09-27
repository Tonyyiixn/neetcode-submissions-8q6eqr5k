class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_ana = defaultdict(list)
        for s in strs:
            sorted_name = tuple(sorted(s))
            group_ana[sorted_name].append(s)
        
        return list(group_ana.values())
