from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False
        lenRow = len(matrix)-1
        lenColumn = len(matrix[0])-1
        i, j = 0, 0
        if target < matrix[i][j]:
            return result
        while True:
            if i >= lenRow + 1 or j >= lenColumn + 1:
                break
            else:
                if matrix[i][j] == target:
                    result = True
                    break
                if matrix[i][lenColumn] < target:
                    i += 1
                    continue
                if matrix[lenRow][j] < target:
                    j += 1
                    continue
                if matrix[i][j] < target:
                    j += 1
                else:
                    j = 0
                    i += 1
        return result







martrix = [[1]]
target = 0
s = Solution()
print(s.searchMatrix(martrix,target))
