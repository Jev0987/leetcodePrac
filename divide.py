'''
    1.是否达到除法要求，若被除数为0或小于除数则返回0

    2.两个数各自都看里头有多少个2的次方
        1）先看除数，需要乘多少个2才能比被除数大，左移一位即乘2。记录乘的次数i；
        2）若大于被除数，记录2的i-1次 + 剩余被除数减去除数乘2的i-1倍的数值继续做减法
'''

class Solution:
    def divide(self, dividend, divisor):
        i, a, b = 0, abs(dividend), abs(divisor)
        if a == 0 or a < b:
            return 0
        while b <= a:
            b = b << 1
            i = i + 1
        else:
            res = (1 << (i - 1)) + self.divide(a - (b >> 1), abs(divisor))
            if (dividend ^ divisor) < 0:
                res = -res
            return min(res, (1 << 31) - 1)


s = Solution()
print(s.divide(16, 2))