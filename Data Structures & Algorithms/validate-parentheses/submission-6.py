class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {']':'[',')':'(','}':'{'}
        for op in s:
            if (op in mapping):
                if stack and (mapping[op] == stack[-1]):
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(op)
        
        if stack:
            return False
        else:
            return True