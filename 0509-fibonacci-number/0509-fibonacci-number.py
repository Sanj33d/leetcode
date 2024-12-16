class Solution:
    def fib(self, n: int) -> int:
        if n == 1: # basecase 1
            return n
        elif n == 0: # basecase 2
            return n
        else:
            return self.fib(n-1) + self.fib(n-2) 
    ## once it hits bc, starts returning consecutively
        