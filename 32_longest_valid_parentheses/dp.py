"""
Runtime: 85 ms
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = [0 for _ in range(len(s))]
        for i, c in enumerate(s[1:], start=1):
            if c==")":
                if s[i-1]=="(":
                    longest[i] = Solution.get(longest, i-2, 0) + 2
                else:  # s[i-1]==")"
                    if Solution.get(s, i-longest[i-1]-1, None)=="(":
                        longest[i] = longest[i-1] + 2 + Solution.get(longest, i-longest[i-1]-2, 0)

        return max(longest) if len(longest)>0 else 0

    @staticmethod
    def get(l, i, default):
        return l[i] if i>=0 and i<len(l) else default


if __name__ == "__main__":
    import sys
    print(Solution().longestValidParentheses(sys.argv[1]))
