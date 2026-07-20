# LeetCode 240: 搜索二维矩阵 II (Search a 2D Matrix II)
#
# 矩阵特性：每行从左到右递增，每列从上到下递增。
#
# 核心思路（从右上角开始，Z 字形搜索）：
# 选择右上角作为起点是关键——它既是"当前行最大"，又是"当前列最小"：
#   - 若 matrix[row][col] > target → 当前列以下都更大，直接向左缩一列
#   - 若 matrix[row][col] < target → 当前行左边都更小，直接向下移一行
#   直到找到 target 或行列越界。
#
# 为什么不能从左上角？左上角往右和往下都是变大，不知道往哪走，会多出两条分支。
# 右上角/左下角才有"一边大一边小"的方向性，每次排除一行或一列。
#
# 时间复杂度：O(rows + columns)，最坏情况从右上走到左下
# 空间复杂度：O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]  # m×n 矩阵，行列分别递增
        :type target: int
        :rtype: bool                   # 是否存在 target
        """
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        columns = len(matrix[0])

        row = 0                   # 从第一行开始
        column = columns - 1      # 从最后一列开始（右上角）

        # 边界：行不能超过底部，列不能超过左侧
        while row < rows and column >= 0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                # 当前值比目标大 → 当前列以下的所有值只会更大 → 排除整列
                column -= 1
            else:
                # 当前值比目标小 → 当前行左边的所有值只会更小 → 排除整行
                row += 1

        return False
