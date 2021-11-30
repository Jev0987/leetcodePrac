
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        A = ''
        Max = 0
        left = 0
        right = 0
        #右指针不断向后遍历，若遇到相同的字符时，左指针右移，子串A减少一个字符
        while(right < len(s)):
            #左右指针相同时：1.开始位置；2.由于子串一直有相同元素，导致左右指针重合
            if left == right:
                A = A + s[right]
                right = right + 1
                if Max < len(A):
                    Max = len(A)
                continue
            #若字符不存在于子串A中，将字符添加进A，并计算最大值，右指针往后
            if s[right] not in A:
                A = A + s[right]
                if Max < len(A):
                    Max = len(A)
                right = right + 1
            #字符存在于A中，删除A中的字符，并使左指针右移
            else:
                A = A.lstrip(s[left])
                left = left + 1
        return Max



s = "bbbbb"
S = Solution()
print(S.lengthOfLongestSubstring(s))