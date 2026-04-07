class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = {}

        for s in strs:
            fingerprint = "".join(sorted(s))

            if fingerprint not in anagram_map:
                anagram_map[fingerprint] = []
            
            anagram_map[fingerprint].append(s)
        

        return list(anagram_map.values())

        