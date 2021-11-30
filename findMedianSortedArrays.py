from typing import List

#原题是要达到log(m+n)的时间复杂度
#参照之前88题合并数组，最终找到中位数
#注意其他解法，如分治法

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = {}
        sumCount = len(nums1) + len(nums2)
        n1 , n2 , index = 0, 0, 0
        while(n1 < len(nums1) and n2 < len(nums2)):
            if(nums1[n1] < nums2[n2]):
                arr[index] = nums1[n1]
                n1 += 1
            else:
                arr[index] = nums2[n2]
                n2 += 1
            index += 1
        while(n1 < len(nums1)):
            arr[index] = nums1[n1]
            n1 += 1
            index += 1
        while(n2 < len(nums2)):
            arr[index] = nums2[n2]
            n2 += 1
            index += 1

        #Python “//” 取整 除
        if(sumCount % 2 != 0):
            return round(arr[sumCount//2],5)
        else:
            return round((arr[sumCount//2] + arr[sumCount//2 - 1])/2,5)

S = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(S.findMedianSortedArrays(nums1,nums2))
