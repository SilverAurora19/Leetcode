# 螺旋矩阵（LeetCode 54）。
# 将 n×n 矩阵顺时针旋转 90°，分两步：
#
# 核心思路（转置 + 水平翻转）：
# 顺时针旋转 90° 等价于：先沿主对角线转置，再把每一行翻转。
#
# 例如：
#   [1, 2, 3]      转置    [1, 4, 7]    每行翻转    [7, 4, 1]
#   [4, 5, 6]  ————→      [2, 5, 8]  ——————→      [8, 5, 2]
#   [7, 8, 9]            [3, 6, 9]              [9, 6, 3]
#
# 时间复杂度：O(n²)
# 空间复杂度：O(1)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]    # n×n 方阵
        :rtype: None                     # 原地旋转
        """
        n = len(matrix)

        # 第1步：沿主对角线转置（左上→右下的对角线）
        # 只需遍历右上三角区域（column 从 row+1 开始），避免重复交换
        for row in range(n):
            for column in range(row + 1, n):
                # 交换 matrix[row][column] 和 matrix[column][row]
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row], matrix[row][column]
                )

        # 第2步：每一行进行水平翻转（reverse）
        for row in range(n):
            left = 0
            right = n - 1

            while left < right:
                # 交换该行左右两端的元素
                matrix[row][left], matrix[row][right] = (
                    matrix[row][right], matrix[row][left]
                )
                left += 1
                right -= 1
