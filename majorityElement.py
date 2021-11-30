from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        box = defaultdict(int)
        n = len(nums)
        times = n//3
        reslut = []
        for i in nums:
            box[i] += 1

        for j, k in box.items():
            if k > times:
                reslut.append(j)

        return reslut





l = [1]
s = Solution()
print(s.majorityElement(l))
