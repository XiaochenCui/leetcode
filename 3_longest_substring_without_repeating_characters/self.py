class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        maxLength = 0
        left, right = 0, 0
        for i, c in enumerate(s):
            right = i
            if c in d:
                left = max(left, d[c] + 1)
            d[c] = right
            maxLength = max(maxLength, right-left+1)
        return maxLength


if __name__ == "__main__":
    import sys
    print(Solution().lengthOfLongestSubstring(sys.argv[1]))
