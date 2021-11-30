

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        if n % 2 == 0:
            n /= 2
            return 1 + self.integerReplacement(n)
        else:
            return 2 + min(self.integerReplacement((n - 1)//2), self.integerReplacement((n + 1)//2))




n = 8
s = Solution()
print(s.integerReplacement(n))
