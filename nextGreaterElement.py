from collections import defaultdict
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        i = 0
        while True:
            if i > len(nums1) - 1:
                break
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    if j == len(nums2) - 1:
                        l.append(-1)
                        break
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            l.append(nums2[k])
                            break
                        if k == len(nums2) - 1:
                            l.append(-1)


            i += 1
        return l

# 答案：单调栈 + 哈希表
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         #结果使用哈希表存储
#         res = {}
#         stack = []
#         for num in reversed(nums2):#逆序判断nums2中的值
#             #若栈不为空且当前逆序的nums2的值大于栈底元素
#             while stack and num >= stack[-1]:
#                 stack.pop()
#             #当前对应值的下一个更大元素为栈顶元素，若栈无元素则为-1
#             res[num] = stack[-1] if stack else -1
#             stack.append(num)
#         return [res[num] for num in nums1]






nums1 = [4,1,2]
nums2 = [1,3,4,2]
s = Solution()
print(s.nextGreaterElement(nums1,nums2))
