from copy import deepcopy

from tools.print import print_split
from tools.time import timeit


class Solution(object):
    def __init__(self):
        self.board = []
        self.boards = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.solve_line(0, n)
        return self.boards

    def solve_line(self, row, n):
        if row == n:
            self.boards.append([''.join(i) for i in self.board])
            return
        else:
            for col in range(n):
                if self.is_valid(row, col, n):
                    self.board[row][col] = 'Q'
                    self.solve_line(row + 1, n)
                    self.board[row][col] = '.'

    def is_valid(self, row, col, n):
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True


s = Solution()
for i in s.solveNQueens(4):
    print(i)
    print_split()
