from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        digits[n] += 1
        result = []
        while(digits[n] == 10):
            if n == 0:
                result.append(1)
                result.append(0)
                for i in range(1, len(digits)):
                    result.append(digits[i])
                return result
            digits[n] = 0
            digits[n - 1] += 1
            n -= 1

        return digits



l = [9,]
s = Solution()
print(s.plusOne(l))
