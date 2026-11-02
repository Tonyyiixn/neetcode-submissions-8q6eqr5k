class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(1,1+length):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[length]