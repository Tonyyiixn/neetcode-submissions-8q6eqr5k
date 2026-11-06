class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        for i in range(0,n+1):
            x = i
            while x:
                output[i]+= (x&1)
                x >>= 1
        
        return output

