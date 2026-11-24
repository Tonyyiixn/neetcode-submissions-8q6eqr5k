class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for s in strs:
            ana_dict[tuple(sorted(s))].append(s)
        
        return list(ana_dict.values())