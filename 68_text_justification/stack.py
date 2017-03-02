"""
Runtime: 58 ms
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        while len(words) > 0:
            stack = []
            while len(words)>0 and Solution.length(stack+[words[0]]) + len(stack) <= maxWidth:
                stack.append(words.pop(0))

            if words and len(stack)>1:
                spacesSum = maxWidth - Solution.length(stack)
                groupNum = len(stack) - 1
                quotient, remainder = divmod(spacesSum, groupNum)

                sentense = (" "*(quotient+1)).join(stack[:remainder+1]) + " "*quotient + (" "*quotient).join(stack[remainder+1:])
            else:
                sentense = " ".join(stack).ljust(maxWidth)

            result.append(sentense)

        return result


    @staticmethod
    def length(list):
        return sum([len(i) for i in list])


if __name__ == "__main__":
    words = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
    l = 30
    print(Solution().fullJustify(words, l))
