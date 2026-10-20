class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)
        for ch in s:
            char_count[ch] += 1
        for ch in t:
            char_count[ch] -= 1
        
        for count in char_count.values():
            if count != 0:
                return False
        
        return True
