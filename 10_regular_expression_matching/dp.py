"""
Runtime: 159 ms
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        if n==0:
            return m==0

        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = False
        for j in range(1, n+1):
            dp[0][j] = j>1 and p[j-1]=='*' and dp[0][j-2]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
                else:  # p[j-1] == '*'
                    dp[i][j] = dp[i][j-2] or (s[i-1]==p[j-2] or p[j-2]=='.') and dp[i-1][j]

        return dp[m][n]
