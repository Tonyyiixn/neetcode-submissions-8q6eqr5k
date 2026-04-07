class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)

        for s in strs:
            fingerprint = "".join(sorted(s))

            anagram_map[fingerprint].append(s)
        

        return list(anagram_map.values())

        