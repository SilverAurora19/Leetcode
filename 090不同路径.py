# LeetCode 62: 不同路径 (Unique Paths)
#
# 题目：机器人从 m×n 网格的左上角出发，只能向右或向下走，
# 问有多少条不同路径到达右下角。
#
# 核心思路（动态规划）：
# dp[i][j] = 到达格子 (i, j) 的路径数。
#
# 递推公式：
#   dp[i][j] = dp[i-1][j] + dp[i][j-1]
#   到达 (i,j) 只有两种来源：从上面来（向下走一步），或从左边来（向右走一步）。
#
# 边界：
#   第一行和第一列的格子都只有 1 条路径（只能一直往右，或一直往下）。
#
# 例如：m=3, n=3
#   1  1  1
#   1  2  3
#   1  3  6
#   dp[2][2] = 6 条路径
#
# 时间复杂度：O(m × n)
# 空间复杂度：O(m × n)——dp 二维数组
# （空间可优化为 O(n)：每行只依赖上一行，用一维数组滚动即可）

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int   # 行数
        :type n: int   # 列数
        :rtype: int    # 不同路径总数
        """
        # dp[i][j] = 到达 (i,j) 的路径数
        dp = [[0] * n for _ in range(m)]

        # 第一行：只能一直向右，路径数为 1
        for j in range(n):
            dp[0][j] = 1

        # 第一列：只能一直向下，路径数为 1
        for i in range(m):
            dp[i][0] = 1

        # 从 (1,1) 开始填充，每个格子 = 上方 + 左方
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # 返回右下角的路径数
        return dp[m - 1][n - 1]
