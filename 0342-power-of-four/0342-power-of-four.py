class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        def helper(n):
            if n == 1: # basecase 1
                return True
            elif n % 4 != 0: # basecase 2 [trap state]
                return False
            else:
                return helper(n//4)
        return helper(n)
        # once hits any of the bc, starts returning consecutively