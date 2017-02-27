"""
Warning: Time Limit Exceeded
"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        units = ["", "Thousand", "Million", "Billion", "Trillion"]
        i = 0
        words = []
        while num > 0:
            if num%1000 != 0:
                words = Solution._numberToWords(num%1000) + [units[i]] + words
                num //= 1000
                i += 1

        words = filter(lambda i: i!="", words)
        print([i for i in words])
        return " ".join(words)


    @staticmethod
    def _numberToWords(num):
        """
        1 <= num <= 999

        :type num: int
        :rtype: list[str]
        """
        lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                      "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                      "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                      "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num == 0:
            return []
        elif num < 20:
            return [lessThan20[num]]
        elif num < 100:
            return [tens[num//10], lessThan20[num%10]]
        else:
            return [lessThan20[num//100], "Hundred"] + Solution._numberToWords(num%100)


if __name__ == "__main__":
    import sys
    print(Solution().numberToWords(int(sys.argv[1])))
