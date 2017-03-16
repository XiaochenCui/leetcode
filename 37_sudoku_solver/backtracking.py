"""
Runtime: 1372 ms
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        board[:] = map(list, board)
        self._solve(board)
        board[:] = map(lambda i: "".join(i), board)

    def _solve(self, board):
        size = len(board)
        for i in range(size):
            for j in range(size):
                if board[i][j] == ".":
                    for v in range(1, 10):
                        if self.isValid(board, i, j, str(v)):
                            board[i][j] = str(v)
                            if self._solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def isValid(self, board, row, col, val):
        if val in board[row][:col]+board[row][col+1:]:
            return False
        for i in range(len(board)):
            if row!=i and board[i][col]==val:
                return False
        for i in range(row/3*3, row/3*3+3):
            for j in range(col/3*3, col/3*3+3):
                if i!=row and j!=col and board[i][j]==val:
                    return False
        return True


if __name__ == "__main__":
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    Solution().solveSudoku(board)
