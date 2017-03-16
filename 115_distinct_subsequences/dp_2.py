"""
Runtime: 172 ms
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [0 for _ in range(len(t)+1)]
        for j in range(1, len(s)+1):
            pre = dp[0] = 1
            for i in range(1, len(t)+1):
                temp = dp[i]
                if s[j-1]==t[i-1]:
                    dp[i] = dp[i] + pre
                else:
                    dp[i] = dp[i]
                pre = temp
        return dp[-1]
