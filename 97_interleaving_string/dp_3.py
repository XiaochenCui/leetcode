"""
DP solution
O(n) space

Runtime: 56 ms
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        因为 dp.py 中每次内循环只用到 table[i-1] 和 table[i],
        所以这里简化为用两个一维数组
        per = table[i-1]
        cur = table[i]

        因为 dp_2.py 中每次内循环只用到 cur[j-1] 和 pre[j],
        所以这里简化为一个一维数组
        dp[j-1] = cur[j-1]
        dp[j] = pre[j]

        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1)+1, len(s2)+1, len(s3)+1
        if l1+l2 != l3+1:
            return False

        dp = [True for _ in range(l2)]
        for j in range(1, l2):
            dp[j] = dp[j-1] and s2[j-1]==s3[j-1]

        for i in range(1, l1):
            dp[0] = dp[0] and s1[i-1]==s3[i-1]
            for j in range(1, l2):
                dp[j] = (dp[j-1] and s2[j-1]==s3[i+j-1]) or \
                    (dp[j] and s1[i-1]==s3[i+j-1])

        return dp[-1]


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3s = ["aadbbcbcac",
           "aadbbbaccc"]
    for s3 in s3s:
        print(Solution().isInterleave(s1, s2, s3))

