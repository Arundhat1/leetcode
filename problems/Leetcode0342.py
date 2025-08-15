class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n & (n-1)) == 0:
            if (n-1) % 3 == 0:
                return True
        
        return False
        
