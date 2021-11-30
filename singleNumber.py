from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        box = {}
        result = []
        for i in nums:
            box[i] += 1

        for i,k in box:
            if k == 1:
                result.append(i)
        return result

nums = [1,2,1,3,2,5]
s = Solution()
print(s.singleNumber(nums))
