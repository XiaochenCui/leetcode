class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        from itertools import zip_longest

        s = ""
        carry = 0
        for i, j in zip_longest(num1[::-1], num2[::-1], fillvalue=0):
            carry, temp = divmod(int(i)+int(j)+carry, 10)
            s = str(temp) + s
        if carry:
            s = "1" + s
        return s


if __name__ == "__main__":
    import sys
    num1, num2 = sys.argv[1], sys.argv[2]
    print(Solution().addStrings(num1, num2))
