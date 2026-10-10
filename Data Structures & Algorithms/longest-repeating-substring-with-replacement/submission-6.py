class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        char_max = 0
        char_set = defaultdict(int)
        for r in range(len(s)):
            char_set[s[r]] += 1
            char_max = max(char_max,char_set[s[r]])

            length = r  - l + 1
            if length - char_max > k:
                char_set[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        
        return longest