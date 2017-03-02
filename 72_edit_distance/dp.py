"""
Runtime: 225 ms
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = list(range(len(word1)+1))

        for j in range(1, len(word2)+1):
            pre = dp[0]
            dp[0] = j
            for i in range(1, len(word1)+1):
                temp = dp[i]
                if word2[j-1] == word1[i-1]:
                    dp[i] = pre
                else:
                    dp[i] = min([pre+1, dp[i]+1, dp[i-1]+1])
                pre = temp

        return dp[-1]


if __name__ == "__main__":
    import sys
    print(Solution().minDistance(sys.argv[1], sys.argv[2]))
