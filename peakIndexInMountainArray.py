from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        index = 0
        for i in range(len(arr)):
            if arr[i - 1] < arr[i]:
                index = i
        return index



l = [1, 3, 5, 3, 2]
l2 = [0, 1, 0]
S = Solution()
print(S.peakIndexInMountainArray(l2))
