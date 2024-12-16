class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        def helper(n):
            if n == 1: # basecase 1
                return True
            elif n % 3 != 0: # basecase 2 [trap state]
                return False
            else:
                return helper(n//3)
        return helper(n)
        # once hits the bc, starts returning consecutively
        