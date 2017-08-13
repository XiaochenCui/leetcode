class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        stack = []
        signs = "+-*/"
        sign = "+"
        num = 0
        for i, c in enumerate(s):
            print(stack)
            if c == " " and i!=len(s)-1:
                continue
            if c not in signs:
                num = num*10+int(c)
            elif c in signs or i==len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(stack.pop()/num)
                sign = c
                num = 0
        return sum(stack)


if __name__ == "__main__":
    import sys
    print(Solution().calculate(sys.argv[1]))
