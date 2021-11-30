import random
from typing import List



class Solution:

    def __init__(self, nums: List[int]):
        self.lt = nums
        self.origent = self.lt.copy()

    def reset(self) -> List[int]:
        nums = self.origent
        return nums

    def shuffle(self) -> List[int]:
        #生成元素都为0 的长度为nums 的数组
        shuffled = [0] * len(self.lt)

        for i in range(len(self.lt)):
            j = random.randrange(len(self.lt))
            #list.pop(index = -1) 移除列表中的一个元素，默认为最后一个元素，并返回该元素值
            shuffled[i] = self.lt.pop(j)
        self.lt = shuffled
        return self.lt



# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
