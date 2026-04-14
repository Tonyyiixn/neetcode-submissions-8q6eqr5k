class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        max_count = 0
        charset = set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
                
            charset.add(s[r])
            max_count = max(max_count,r - l + 1)
        
        return max_count