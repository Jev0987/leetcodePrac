from collections import defaultdict
from typing import List

'''
cases1:
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]

cases2:
输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]

the length of target sub-string is 10

tips:
0 <= s.length <= 105
s[i] 为 'A'、'C'、'G' 或 'T'
'''

#看了答案的， 利用哈希表来处理。原本读题的时候没有发现字串长度必须为10

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        substrs = []
        #哈希表
        cnt = defaultdict(int)
        for i in range(len(s) - L + 1):
            #s 中从i 到i+L的字符
            sub = s[i: i + L]
            #先保存在哈希表中
            cnt[sub] += 1
            #若在哈希表中出现两次，则放入字串list中
            if cnt[sub] == 2:
                substrs.append(sub)

        return substrs






S = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

s = Solution()
print(s.findRepeatedDnaSequences(S))



