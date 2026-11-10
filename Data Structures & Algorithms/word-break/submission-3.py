class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        word_set = set(wordDict)
        for j in range(1,len(s)+1):
            for i in range(j):
                if dp[i] and s[i:j] in word_set:
                    dp[j] = True
                    break
        
        return dp[len(s)]