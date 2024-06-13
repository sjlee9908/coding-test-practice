class Solution:
    def fib(self, n: int) -> int:
        n0 = 0
        n1 = 1
        n2 = None

        if n == 0:
            return 0
        elif n == 1:
            return 1

        for i in range(n - 1):
            n2 = n0 + n1
            n0 = n1
            n1 = n2

        return n2


print(Solution.fib("a", 4))
