from typing import List

#1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        #enumerate函数的使用：将可遍历数据对象组合成索引序列，同时出现数据和数组下标，一般用在for循环中
        #1.先把数组拆成下标位置和数值位置
        #2.在列表中数值对应的下标位置存放它在数组中的信息
        for index,number in enumerate(nums):
            if target - number in tmp:
                return [tmp[target - number],index]
            tmp[number] = index

nums = [1,5,6,9,7]
target = 10
S = Solution()
print(S.twoSum(nums,target))
