class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        #若长度不等，直接返回false
        if len(s) != len(goal):
            return False
        #若两个字符串相等（同）：是否有重复元素，若有，则为True，否则返回False
        #若两个字符串不等（同）：
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False
        #zip()打包为元组列表
        #判断s和goal里位置不同的字符个数必须为2且相同。
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]








s = "aabcc"
goal = "cabac"
obj = Solution()
print(obj.buddyStrings(s,goal))
