"""
Runtime: 72 ms
"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        unitCount = 0
        remainder = num
        words = []
        while remainder > 999:
            quotient, remainder = divmod(remainder, 1000)
            if remainder > 0:
                Solution._numberToWords(remainder, words, unitCount)

            remainder = quotient
            unitCount += 1

        Solution._numberToWords(remainder, words, unitCount)

        return " ".join(words)

    @staticmethod
    def _numberToWords(num, words, unitCount):
        """
        1 <= num <= 999

        :type num: int
        """
        tempWords = []
        mod100, mod10, mod1 = num//100, num%100//10, num%10
        numbers = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        tenToNineteen = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        units = ["", "Thousand", "Million", "Billion", "Trillion"]

        if mod100:
            tempWords.append(numbers[mod100])
            tempWords.append("Hundred")
        if mod10 > 1:
            tempWords.append(tens[mod10])
            if mod1:
                tempWords.append(numbers[mod1])
        elif mod10 == 1:
            tempWords.append(tenToNineteen[num%100-10])
        elif mod1:
            tempWords.append(numbers[mod1])

        # add unit
        if unitCount > 0:
            tempWords.append(units[unitCount])

        # insert left
        words[:0] = tempWords

        return


if __name__ == "__main__":
    import sys
    print(Solution().numberToWords(int(sys.argv[1])))
