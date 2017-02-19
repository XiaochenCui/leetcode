class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        return self.uniquePathsInLocation(obstacleGrid, len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)

    def uniquePathsInLocation(self, obstacleGrid, row, col):
        if obstacleGrid[row][col] == 1:
            return 0
        elif row == 0 and col == 0:
            return 1
        elif row == -1 or col == -1:
            return 0
        else:
            return self.uniquePathsInLocation(obstacleGrid, row - 1, col) + self.uniquePathsInLocation(obstacleGrid,
                                                                                                       row, col - 1)


if __name__ == '__main__':
    s = Solution()
    grid = [
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    r = s.uniquePathsWithObstacles(grid)
    print r
