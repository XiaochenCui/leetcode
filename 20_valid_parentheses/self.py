class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: boolgg
        """
        match = {')': '(',
                 ']': '[',
                 '}': '{'}
        stack = []
        for i in s:
            if i not in match:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif match[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if len(stack)==0 else False


if __name__ == "__main__":
    import sys
    print(Solution().isValid(sys.argv[1]))
