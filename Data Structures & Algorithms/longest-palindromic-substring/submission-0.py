class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. Tracker for our "best so far"
        longest_word = ""

        # 2. The Helper Function (You will build the logic inside this!)
        def expand(left: int, right: int) -> str:
            # The goal here is a while loop:
            # As long as left and right are in bounds AND s[left] == s[right]:
            while left >= 0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
            #    step left backwards (left -= 1)
            #    step right forwards (right += 1)
            # 
            # Once they stop matching, return the sliced string!

        # 3. The Main Loop (Walk through every single letter)
        for i in range(len(s)):
            
            # Try to grow an Odd length palindrome (Center is 1 letter: i)
            odd_pal = expand(i, i)
            
            # Try to grow an Even length palindrome (Center is 2 letters: i and i+1)
            even_pal = expand(i, i + 1)
            
            # 4. Check if we found a new champion
            if len(odd_pal) > len(longest_word):
                longest_word = odd_pal
                
            if len(even_pal) > len(longest_word):
                longest_word = even_pal
                
        return longest_word