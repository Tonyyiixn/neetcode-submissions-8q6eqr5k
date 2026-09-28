class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op_dict = {')':'(',']':'[','}':'{'}
        for o in s:
            if o in op_dict:
                if stack and op_dict[o] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(o)
        
        if stack:
            return False
        else:
            return True