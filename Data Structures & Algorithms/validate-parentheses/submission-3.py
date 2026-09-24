class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(','}':'{',']':'['}
        for o in s:
            if o in mapping:
                if stack and stack[-1] == mapping[o]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(o)
            
        if stack:
            return False
        else:    
            return True
