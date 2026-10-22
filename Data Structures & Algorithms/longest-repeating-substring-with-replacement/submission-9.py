class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        max_char = 0
        char_count = defaultdict(int)
        for r in range(len(s)):
            char_count[s[r]] += 1
            max_char = max(max_char,char_count[s[r]])

            length = r - l + 1
            if length - max_char > k:
                char_count[s[l]] -= 1
                l += 1
            
            longest = max(longest,r - l + 1)
        
        return longest