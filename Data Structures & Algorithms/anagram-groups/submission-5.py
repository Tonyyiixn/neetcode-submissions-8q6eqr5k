class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_ana = defaultdict(list)
        for word in strs:
            placeholder = tuple(sorted(word))
            group_ana[placeholder].append(word)
        
        return list(group_ana.values())