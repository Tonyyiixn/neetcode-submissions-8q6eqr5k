class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_default = defaultdict(list)
        for s in strs:
            s_default[tuple(sorted(s))].append(s)
        
        return list(s_default.values())