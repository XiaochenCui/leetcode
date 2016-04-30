# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]


    def next(self):
        """
        :rtype: int
        """
        self.hasNext()  # 调用hasNext函数，将指针移动到将要访问的整数
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1  #指针后移一位
        return nestedList[i].getInteger()



    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):    # 如果指针越界，将当前list移出stack
                s.pop()
            else:
                x = nestedList[i]   # 获取list x
                if x.isInteger():   # 如果 x 为整数，return
                    return True
                s[-1][1] += 1   # 将当前 list x 压入stack，并将当前指针 +1
                s.append([x.getList(), 0])  
        return False



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())