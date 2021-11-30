
class Solution:
    def numberToWords(self, num: int) -> str:
        numName1 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        numName2 = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
        numName3 = ['Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        numName4 = ['Hundred', 'Thousand', 'Million', 'Billion']
        result = ''
        if num == 0:
            return "Zero"

        if num <= 10:
            result = numName1[num - 1]
        elif num < 20:
            result = numName2[num - 11]
        elif num < 100:
            result = numName3[num // 10 - 2] + ' ' + numName1[(num % 10) - 1]
        elif



        return ""


S = 123

s = Solution()
s.numberToWords(S)