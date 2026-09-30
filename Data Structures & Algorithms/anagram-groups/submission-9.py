class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dic = defaultdict(list)
        for s in strs:
            ana_dic[tuple(sorted(s))].append(s)
        
        return list(ana_dic.values())