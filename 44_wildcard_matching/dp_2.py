class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [False for _ in p]
        dp[:0] = [True]
        for j in range(1, len(p)+1):
            dp[0] = dp[0] and p[j-1]=="*"
            for i in range(1, len(s)+1):
                if p[j-1] != "*":
                    dp[i] = s[i-1]==p[j-1] or p[j-1]=="?"
                else:
                    dp[i] = dp[i] or dp[i-1]

        return bool(dp[-1])


if __name__ == "__main__":
    import sys
    print(Solution().isMatch(sys.argv[1], sys.argv[2]))
