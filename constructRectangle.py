from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = []
        tmp = []
        if area == 1:
            l = [1, 1]
            return l
        for i in range(1,area//2 +1):
            if area % i == 0:
                tmp.append(i)

        W = tmp[len(tmp)//2]
        L = area//W
        l.append(L)
        l.append(W)


        return l



s = Solution()
print(s.constructRectangle(1))

# 官方答案，使用sqrt方法
# class Solution:
#     def constructRectangle(self, area: int) -> List[int]:
#         w = int(sqrt(area))
#         while area % w:
#             w -= 1
#         return [area // w, w]