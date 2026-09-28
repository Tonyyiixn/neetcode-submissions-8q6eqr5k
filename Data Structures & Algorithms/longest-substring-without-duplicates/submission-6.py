class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        set_char = set()
        for r in range(len(s)):
            while s[r] in set_char:
                set_char.remove(s[l])
                l += 1

            set_char.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest