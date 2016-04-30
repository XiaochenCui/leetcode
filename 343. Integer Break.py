class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 1:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return int(pow(3, n / 3))
        if n % 3 == 1:
            return int(pow(3, (n - 4) / 3) * 4)
        if n % 3 == 2:
            return int(pow(3, (n - 2) / 3) * 2)

s = Solution
n = int(input('enter a positive number:\n'))
print(s.integerBreak(s, n))
