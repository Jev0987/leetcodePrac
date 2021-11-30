

class Solution:
    def findComplement(self, num: int) -> int:
        binnum = bin(num)
        binlist = list(binnum)
        for i in range(2, len(binlist)):
            if binlist[i] == "1":
                binlist[i] = "0"
            else:
                binlist[i] = "1"

        binstr = "".join(binlist)
        tennum = int(binstr, 2)

        return tennum


# print(bin(5))
# for i in range(2, len(bin(5))):
#     print(bin(5)[i])

s = Solution()
print(s.findComplement(5))