class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        istr = []

        for i in range(len(s)):
            istr.append(s[i])
        
        for j in range(len(t)):
            if t[j] in istr:
                istr.remove(t[j])
            else:
                return False

        return not istr
