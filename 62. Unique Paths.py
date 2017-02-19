class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N = m + n - 2
        k = m - 1
        res = 1
        for i in range(1, k + 1):
            res *= float(N - k + i)/i
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.uniquePaths(4, 4)
    print(res)
