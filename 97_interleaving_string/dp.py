"""
DP solution
O(m*n) space

Runtime: 276 ms
"""
import numpy as np


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        table[i, j] == True => s3[i+j-1] is formed by the interleaving of s1[i-1] and s2[j-1]

        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False

        table = np.zeros((len(s1)+1, len(s2)+1), dtype=np.int16)
        for i1 in range(len(s1)+1):
            for i2 in range(len(s2)+1):
                if i1==0 and i2==0:
                    table[i1][i2] = True
                elif i1==0:
                    table[i1][i2] = (table[i1][i2-1] and s2[i2-1]==s3[i1+i2-1])
                elif i2==0:
                    table[i1][i2] = (table[i1-1][i2] and s1[i1-1]==s3[i1+i2-1])
                else:
                    table[i1][i2] = (table[i1][i2-1] and s2[i2-1]==s3[i1+i2-1]) or (table[i1-1][i2] and s1[i1-1]==s3[i1+i2-1])

        return bool(table[len(s1)][len(s2)])


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3s = ["aadbbcbcac",
           "aadbbbaccc"]
    for s3 in s3s:
        print(Solution().isInterleave(s1, s2, s3))
