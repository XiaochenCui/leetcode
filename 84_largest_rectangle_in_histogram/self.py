"""
Runtime: 126 ms
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        # stack 用来记录高度递增序列
        # stack:
        # [1]
        # [1, 2]
        # [1, 2, 3]
        # [1, 4]
        # [1, 4, 5]
        # [6]
        stack = [0]
        r = 0
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                r = max(r, w*h)
            stack.append(i)
        return r


if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(Solution().largestRectangleArea(heights))
