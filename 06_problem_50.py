class Solution(object):
   def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        memo = {}

        def power(x, n):
            if n == 0:
                return 1
            if n in memo:
                return memo[n]
            half = power(x, n // 2)
            if n % 2 == 0:
                memo[n] = half * half
            else:
                memo[n] = half * half * x
            return memo[n]

        return power(x, n)