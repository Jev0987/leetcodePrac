from typing import List

# #结果超时了！！！
# class Solution:
#     def minMoves(self, nums: List[int]) -> int:
#         n = len(nums)
#         #插入排序
#         def sorted(nums):
#             for i in range(1, len(nums)):
#                 key = nums[i]
#                 j = i - 1
#                 while j >= 0 and key < nums[j]:
#                     nums[j + 1] = nums[j]
#                     j -= 1
#                 nums[j + 1] = key
#
#         #判断元素是否相等
#         def isSame(nums):
#             l = len(nums)
#             result = True
#             for i in range(l):
#                 if i == l - 1:
#                     break
#                 if nums[i] == nums[i + 1]:
#                     continue
#                 else:
#                     result = False
#             return result
#
#         def cal(nums, n):
#             count = 0
#             #每次都排序，将前n-1个数字+1，记录次数
#             sorted(nums)
#             #判断整个数列是否相等
#             while(bool(1 - isSame(nums))):
#                 #前n-1个+1
#                 for i in range(n - 1):
#                     nums[i] += 1
#                 count += 1
#                 sorted(nums)
#             return count
#
#         return cal(nums, n)


#每次考虑n-1个做加法，不如每次考虑1个做减法，直至所有元素相同

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        res = 0
        for num in nums:
            #每次那个1元素需减多少次，全部的累计起来
            res += num - min_num
        return res



l = [1,1,1]
s = Solution()
print(s.minMoves(l))
