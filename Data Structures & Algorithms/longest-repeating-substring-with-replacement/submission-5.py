class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        max_char = 0
        char_set = {}
        for r in range(len(s)):
            char_set[s[r]] = char_set.get(s[r],0) + 1
            max_char = max(max_char,char_set[s[r]])

            length = r - l + 1
            if length - max_char > k:
                char_set[s[l]] -= 1
                l += 1
            
            longest = max(longest,r - l + 1)
        
        return longest