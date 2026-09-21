class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = {}
        max_char = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1

            max_char = max(count[s[r]],max_char)

            window_len = r - l + 1

            if window_len - max_char > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest