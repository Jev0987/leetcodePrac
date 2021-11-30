from collections import defaultdict
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, minX, minY, maxX, maxY = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        cnt = defaultdict(int)

        for rect in rectangles:
            x, y, a, b = rect[0], rect[1],  rect[2], rect[3]
            area += (a-x) * (b-y)

            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, a)
            maxY = max(maxY, b)

            cnt[(x,y)] += 1
            cnt[(x,b)] += 1
            cnt[(a,y)] += 1
            cnt[(a,b)] += 1

        if area != (maxX - minX) * (maxY - minY) or cnt[(minX, minY)] != 1 or cnt[(minX, maxY)] != 1 or cnt[(maxX, minY)] != 1 or cnt[(maxX, maxY)] != 1:
            return False

        #del用来删除对象(四个顶点-》降低遍历的数量）
        del cnt[(minX,minY)], cnt[(minX, maxY)], cnt[(maxX,minY)], cnt[(maxX,maxY)]
        #all()用来判断给定的可迭代的参数iterable中的元素是否都为TRUE，如果是返回true ，否则返回false
        return all(c == 2 or c == 4 for c in cnt.values())

rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
s = Solution()
print(s.isRectangleCover(rectangles))
