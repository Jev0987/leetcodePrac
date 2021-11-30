from typing import List

#合并两个有序数组88
#——————》寻找两个有序数组的中位数

#思路，从后往前添加两个数组中的较大值

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # n1 为第一个数组中最后一个含元素的下标值，n2 为第二个数组中含有元素的下标值， index 为数组1的最后位置值（不断往前遍历用）
        n1, n2, index = m - 1, n - 1, len(nums1) - 1
        while(n1 >= 0 and n2 >= 0):
            if(nums1[n1] > nums2[n2]):
                nums1[index] = nums1[n1]
                n1 -= 1
            else:
                nums1[index] = nums2[n2]
                n2 -= 1
            index -= 1

        while(n2 >= 0):
            nums1[index] = nums2[n2]
            n2 -= 1
            index -= 1


nums1 = [-1,3,0,0,0,0,0]
m = 2
nums2 = [0,0,1,2,3]
n = 5
S = Solution()
S.merge(nums1,m,nums2,n)
print(nums1)