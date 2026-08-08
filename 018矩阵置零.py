# LeetCode 73: 矩阵置零 (Set Matrix Zeroes)
#
# 核心思路（用第一行第一列做标记，O(1) 额外空间）：
# 直接用矩阵的第一行和第一列作为"标记数组"：
#   - 若 matrix[i][j] == 0，就把 matrix[i][0] 和 matrix[0][j] 设为 0，表示第 i 行和第 j 列最终都要置零。
#   - 最后根据这些标记来置零内部元素。
#
# 但第一行和第一列本身是否有零需要提前单独记录，否则会被混淆。
#
# 时间复杂度：O(rows × columns)
# 空间复杂度：O(1)
# 先保存首行首列，再用首列标记行、首行标记列；先处理内部，最后处理首行首列。

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None   # 原地修改
        """
        rows = len(matrix)
        columns = len(matrix[0])

        # 第1步：单独记录第一行、第一列是否需要置零
        first_row_has_zero = False
        first_column_has_zero = False

        # 检查第一列是否有 0
        for row in range(rows):
            if matrix[row][0] == 0:
                first_column_has_zero = True
                break

        # 检查第一行是否有 0
        for column in range(columns):
            if matrix[0][column] == 0:          # 遍历第一行的各列
                first_row_has_zero = True
                break

        # 第2步：用第一行和第一列做标记
        # 遍历内部矩阵（跳过第0行和第0列），遇到 0 就把对应第一行和第一列元素置零
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0          # 标记：该行需要置零
                    matrix[0][column] = 0        # 标记：该列需要置零

        # 第3步：根据标记将内部矩阵对应位置置零
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0

        # 第4步：根据提前记录的标记，处理第一行和第一列本身
        if first_row_has_zero:
            for column in range(columns):
                matrix[0][column] = 0           # 整个第一行置零

        if first_column_has_zero:
            for row in range(rows):
                matrix[row][0] = 0              # 整个第一列置零
