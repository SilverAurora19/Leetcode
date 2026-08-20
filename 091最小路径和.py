# LeetCode 64: 最小路径和 (Minimum Path Sum)
#
# 题目：给定 m×n 网格，每个格子有一个非负数字。从左上角走到右下角，
# 只能向右或向下移动，求路径上所有数字之和的最小值。
#
# 核心思路（动态规划）：
# dp[i][j] = 从左上角到达格子 (i,j) 的最小路径和。
#
# 递推公式：
#   dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#   到达 (i,j) 只能从上面或左边来，取两者中路径和更小的那个，再加上当前格的值。
#
# 边界：
#   dp[0][0] = grid[0][0]（起点就是它自己）
#   第一行只能从左往右：dp[0][j] = dp[0][j-1] + grid[0][j]
#   第一列只能从上往下：dp[i][0] = dp[i-1][0] + grid[i][0]
#
# 例如：grid = [[1,3,1],[1,5,1],[4,2,1]]
#   dp 表：
#   1  4  5
#   2  7  6
#   6  8  7
#   最小路径和 = 7（路径 1→3→1→1→1 = 7，或 1→1→4→... 等）
#
# 时间复杂度：O(m × n)
# 空间复杂度：O(m × n)——dp 二维数组（可优化为 O(n)）

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int   # 最小路径和
        """
        m = len(grid)
        n = len(grid[0])

        # dp[i][j] = 到达 (i,j) 的最小路径和
        dp = [[0] * n for _ in range(m)]

        # 起点
        dp[0][0] = grid[0][0]

        # 第一行：只能从左往右累加
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 第一列：只能从上往下累加
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 其他格子：取上方和左方中较小的，加上当前格的值
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]
