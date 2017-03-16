"""
A line is determined by two factors,say y=ax+b
If two points(x1,y1) (x2,y2) are on the same line(Of course).
Consider the gap between two points.
We have (y2-y1)=a(x2-x1),a=(y2-y1)/(x2-x1) a is a rational, b is canceled since b is a constant
If a third point (x3,y3) are on the same line. So we must have y3=ax3+b
Thus,(y3-y1)/(x3-x1)=(y2-y1)/(x2-x1)=a
Since a is a rational, there exists y0 and x0, y0/x0=(y3-y1)/(x3-x1)=(y2-y1)/(x2-x1)=a
So we can use y0&x0 to track a line;

Runtime: 225 ms
"""
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import numpy as np

        l = len(points)
        result = 0
        for i in range(l):
            dic = {None: 1}
            same = 0
            for j in range(i+1, l):
                x = points[i].x - points[j].x
                y = points[i].y - points[j].y
                if x==0 and y==0:
                    same += 1
                    continue
                if x==0:
                    slope = None
                else:
                    slope = np.longdouble(y)/np.longdouble(x)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            result = max(result, max(dic.values())+same)
        return result
