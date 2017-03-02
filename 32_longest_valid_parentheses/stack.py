"""
Runtime: 122 ms
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, longest = len(s), 0
        stack = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif len(stack) > 0 and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            longest = n
        else:
            left, right = 0, n
            while len(stack) > 0:
                left = stack.pop()
                longest = max(longest, right-left-1)
                right = left
            longest = max(longest, right)

        return longest


if __name__ == "__main__":
    import sys
    print(Solution().longestValidParentheses(sys.argv[1]))
