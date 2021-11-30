

'''
    通过单词第一个下标来判断是否出现单词。
    1.该下标为初始下标或者该下标的前下标对应的字符为空格
    2.该下标对应的字符不为空格
'''


class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            '''
                1. i == 0 and s[i] != ' '表示有第一个词
                2. s[i-1] == ' ' and s[i] != ' ',后续接着有单词出现
            '''
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                count += 1
        return count





S = "Hello"
S1 = "Hello, my name is John"
S2 = ""

s = Solution()
print(s.countSegments(S))
