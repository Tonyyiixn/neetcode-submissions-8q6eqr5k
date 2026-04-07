class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = {}

        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            if key not in output:
                output[key] = []
            output[key].append(s)
        
        return list(output.values())

        