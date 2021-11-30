from collections import defaultdict
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        box = defaultdict(int)
        maxcount = 0
        for i in range(len(nums)):
            box[nums[i]] += 1

        if box.values() == 1:
            return maxcount

        key = box.keys()

        for key, value in box.items():
            if key + 1 in box:
                maxcount = max(value+box[key+1], maxcount)

        return maxcount


nums = [1,2,2,3,4,5,1,1,1,1]
s = Solution()
print(s.findLHS(nums))
