from collections import defaultdict

#看了答案的

class Solution:
    def countAndSay(self, n: int) -> str:
        #首先是刚开始的状态
        prev = "1"
        #迭代n次
        for i in range(n - 1):
            curr = ""   #存放这一次的结果
            pos = 0     #当前位置
            start = 0   #开始的位置

            #从当前位置开始，到结果最后一个位置
            while pos < len(prev):
                #当前位置的值等于，起始对比点位置值（！！此步关键！！）
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos += 1
                #将结果保存
                curr += str(pos - start) + prev[start]
                #把起始对比指针位置移动
                start = pos
            #保存状态，继续迭代
            prev = curr

        return prev
